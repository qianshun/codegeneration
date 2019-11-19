import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from codegeneration import mainUI
from codegeneration.mainUI import Ui_MainWindow


class Procedure_data(object):
    pass


class Mainlogic(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Mainlogic, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_clear.clicked.connect(self.button_clearClicked)
        self.pushButton_OK.clicked.connect(self.button_OKClicked)

    def button_clearClicked(self):

        self.textEdit_data.clear()


    def button_OKClicked(self):


        msg = Mainlogic.generationcode(self)

        reply = QMessageBox.information(self, '消息',msg,QMessageBox.Yes ,QMessageBox.Yes)



    def generationcode(self):
        #获取 参数
        mode = self.cBox_mode.currentText()
        packagename=self.lineEdit_packagename.text()

        source_data = self.textEdit_data.toPlainText()


        if source_data.strip() == '':
            return '要生成的PROCEDURE或者TYPE代码不能为空！'


        ####
        """
        resultstr = analysis_sorce_data(mode, source_data)
        self.textEdit_data.setPlainText(resultstr)
        return '生成成功！'
        """
        ###

        #解析sorcre_data

        try:
            resultstr = analysis_sorce_data(mode,source_data)

            self.textEdit_data.setPlainText(resultstr)
            return '生成成功！'
        except Exception as e:
            self.textEdit_data.setPlainText(str(e))
            print(e)
            return '生成失败！'

def gener_mapper(source_data):
    resultstr = ''
    # 验证输入数据

    str = source_data.lower().strip().replace('\n', '')
    str = str.replace('procedure', '')
    strlist = str.split('(')
    resultstr = 'CALL ' + strlist[0] + '('
    strlist = strlist[1].split(')')
    strlist = strlist[0].split(',')
    # 参数部分
    resultpara = ''
    for value in strlist:
        # print(value)
        str1 = value.split()
        if 'varchar' == str1[2]:
            type = 'VARCHAR'
        else:
            type = 'ARRAY'
        print(str1)
        resultpara = resultpara + str1[0] + ' =>#{' + str1[0] + ',mode=' + str1[
            1].upper() + ',jdbcType=' + type + '},\n'

    resultstr = resultstr + resultpara[:-2] + ')'
    return resultstr

def gener_typehandler(source_data):
    resultstr = ""

    source_data = re.sub('(\(\d+\))',
                      '', source_data, flags=re.IGNORECASE)
    #print(source_data)


    str2 = source_data.lower().strip().replace('\n', '')
    strlist = str2.split('(')

    str2 = strlist[0].replace('type', '').replace('is', '').replace('record', '').strip()
    type_name = str2.title()

    resultstr='import oracle.sql. *;\
    import org.apache.ibatis.type.JdbcType;\
    import org.apache.ibatis.type.TypeHandler;\
    import java.sql. *;\
    import java.util.ArrayList;\
    import java.util.HashMap;\
    import java.util.List;\
    import java.util.Map;\n'
    resultstr =  resultstr+'public class '+type_name+'TypeHandler implements TypeHandler {\
                                                                @Override\
                                                                public Object getResult(ResultSet rs, String columnName) throws SQLException {\
                                                                    return null;\
                                                                }\
                                                                @Override\
                                                                public Object getResult(ResultSet rs, int columnIndex) throws SQLException {\
                                                                    return null;\
                                                                }\
                                                                @Override\
                                                                public void setParameter(PreparedStatement ps, int i, Object parameter, JdbcType jdbcType) throws SQLException {\
                                                                    List<'+type_name+'> objects= (List<'+type_name+'>) parameter;\
                                                                    StructDescriptor structdescriptor = StructDescriptor.createDescriptor("'+type_name+'", ps.getConnection());\
                                                                    STRUCT[] structs = new STRUCT[objects.size()];\
                                                                    for (int index = 0; index < objects.size(); index++) {'

    str_propertys = strlist[1].split(')')[0]
    strlist = str_propertys.split(',')
    result_propertys = type_name+' item = objects.get(index);\
                        Object[] record = new Object['+str(len(strlist))+'];'
    i=0
    result_propertys1=''
    result_propertys2 = ''

    for str_property in strlist:
        str1 = str_property.strip()
        str_property_single_list= str1.split()
        #print(str_property_single_list[0])
        #print(str_property_single_list[1])
        #result_propertys= result_propertys+'record['+str(i)+'] = item.get'+str_property_single_list[0].title()+'();'
        result_propertys = result_propertys + 'record[' + str(i) + '] = item.get' + str_property_single_list[0].replace('_', '').upper() + '();'

        result_propertys1=result_propertys1+type_name+'.'+str_property_single_list[0]+','
        #result_propertys2=result_propertys2+type_name.lower()+'.set'+str_property_single_list[0].title()+'((String)struceAttr['+str(i)+']);'
        result_propertys2 = result_propertys2 + type_name.lower() + '.set' + str_property_single_list[0].replace('_', '').upper() + '((String)struceAttr[' + str(i) + ']);'
        i+=1
    result_propertys1=result_propertys1[:-1]
    resultstr=resultstr+result_propertys+'STRUCT struct = new STRUCT(structdescriptor,ps.getConnection(),record);\
            structs[index]=struct;\
        }\
        ArrayDescriptor desc = ArrayDescriptor.createDescriptor("'+type_name+'",ps.getConnection());\
        ARRAY oracleArray = new ARRAY(desc,ps.getConnection(),structs);\
        ps.setArray(i,oracleArray);\
    }'

    resultstr = resultstr + ' @Override\
    public Object getResult(CallableStatement cs, int columnIndex) throws SQLException {\
        return  convertSqlResult(cs.getObject(columnIndex));\
    }\
    Object convertSqlResult(Object sqlResult) throws SQLException {\
        if (sqlResult instanceof Array) {\
            Object[] structs = (Object[]) ((Array) sqlResult).getArray();\
            List<'+type_name+'> result = new ArrayList<>(structs.length);\
            for (Object struct : structs) {\
                result.add(convertTo'+type_name+'Dao((Struct) struct));\
            }\
            return result;\
        } else if (sqlResult instanceof Struct) {\
            return convertTo'+type_name+'Dao((Struct) sqlResult);\
        } else {\
            throw new SQLException("Unsupported parameter type: " + sqlResult.getClass().getCanonicalName()\
                    + " for handler " + this.getClass().getCanonicalName());\
        }\
    }\
    private Struct convertToDbStruct(Connection connection, '+type_name+' object) throws SQLException {\
        Object[] structFields = new Object[]{'+result_propertys1+'};\
        return connection.createStruct("'+type_name+'", structFields);\
    }\
    private '+type_name+' convertTo'+type_name+'Dao(Struct struct) throws SQLException {\
        '+type_name+'  '+type_name.lower()+' = new '+type_name+'();\
        Object[] struceAttr = struct.getAttributes();'

    resultstr = resultstr + result_propertys2+'return '+type_name+';\
    }\
    }'


    return  resultstr

def gener_pojo(source_data):
    resultstr = ''
    source_data = re.sub('(\(\d+\))',
                         '', source_data, flags=re.IGNORECASE)
    # print(source_data)

    str2 = source_data.lower().strip().replace('\n', '')
    strlist = str2.split('(')
    # create or replace
    str2 = strlist[0].replace('type', '').replace('is', '').replace('record', '').replace('table', '').strip()
    type_name = str2.title()
    resultstr='public class '+type_name+' {'
    str_propertys = strlist[1].split(')')[0]
    strlist = str_propertys.split(',')
    i = 0
    result_propertys1 = ''
    result_propertys2 = ''

    for str_property in strlist:
        str1 = str_property.strip()
        str_property_single_list = str1.split()
        result_propertys1=result_propertys1+'private String '+str_property_single_list[0]+';'
        result_propertys2=result_propertys2+'public String get'+str_property_single_list[0].title()+'() {\
                                                return '+str_property_single_list[0]+';\
                                            }\
                                            public void set'+str_property_single_list[0].title()+'(String '+str_property_single_list[0]+') {\
                                                this.'+str_property_single_list[0]+' = '+str_property_single_list[0]+';\
                                            }'

    resultstr=resultstr+result_propertys1+result_propertys2+'}'

    return resultstr



def analysis_sorce_data(mode, source_data):
    resultstr=''
    if mode == '生成mapper':
        resultstr=gener_mapper(source_data)
    elif mode == '生成typehandler':
        resultstr = gener_typehandler(source_data)
    elif mode == '生成pojo类':
        resultstr = gener_pojo(source_data)

    return resultstr




