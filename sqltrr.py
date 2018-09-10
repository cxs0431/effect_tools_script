# coding=ansi
import os

def getDirList( p ):
	p = str( p )
	if p=="":
		return [ ]
	p = p.replace( "/","\\")
	if p[ -1] != "\\":
		p = p+"\\"
	a = os.listdir( p )
	b = []
	for x in a:
		if os.path.isdir( p + x ):
			b += getDirList( p + x )
	b += [ (p , x)   for x in a if os.path.isfile( p + x ) ]
	return b

s = os.getcwd()
trr = getDirList( s );
file = open(s + '\\Q_���ݿ��ύ��Χ' + '.bat','w')

b_ygt = 0
for (pa,fi) in trr:
	p = pa+fi
	if p.find('KDOP') > -1 or p.find('YGT')>-1:
		b_ygt = 1
		break
lib = 'kbssacct'
for (pa,fi) in trr:
	p = pa+fi
	#if p.find('KDTYZH') <0 and p.find('KBSSACCT')<0:
	#	lib = 'run'
	#	break		
		
if b_ygt:
	file.write( "rem �ύǰ�뽫SQL_SERVER  SQL_USER SQL_PW�滻Ϊ��Ӧ������������ִ��ǰ��ȷ�ϵ�һ�������������ļ� \n")
	file.write( " set SQL_SERVER=xxxx \r\n")
	file.write( " set SQL_USER=xxx  \r\n")
	file.write( " set SQL_PW=xxxxx  \r\n")
	
	currdir = ''
	for (pa,fi) in trr:
		p = pa+fi
		p = p.replace( s,"")
		if currdir != pa:
			currdir = pa
			file.write( " pause  \r\n")
			file.write( " \r\n")
			file.write( " \r\n")
			file.write( " @ECHO ------------------------------------------------------------------------ \r\n")
			file.write( " @ECHO    ��ʼ�ύ:      "+ pa+"  \r\n")
			file.write( " @ECHO ------------------------------------------------------------------------ \r\n")
		lib = 'YGT'
		if pa.find('KIDM') > -1:	
			lib = 'kidm'
		if p.find('.sql') > -1:	
			file.write( '  sqlcmd  -S%SQL_SERVER% -U%SQL_USER% -P%SQL_PW% -d '+lib+' -i ".'+p+ '" -r -o '+p[1:].replace( "\\","_").replace( ".","_")+".log    \r\n")
	
else:
	file.write( "rem �ύǰ�뽫-Sxxxx -Uxx -Pxxx�滻Ϊ���ݿ����Ӳ��� \r\n")
	currdir = ''
	for (pa,fi) in trr:
		p = pa+fi
		p = p.replace( s,"")
		if currdir != pa:
			currdir = pa
			file.write( " pause  \r\n")
			file.write( " \r\n")
			file.write( " \r\n")
			file.write( " @ECHO ------------------------------------------------------------------------ \r\n")
			file.write( " @ECHO    ��ʼ�ύ:      "+ pa.replace( s,"")+"  \r\n")
			file.write( " @ECHO ------------------------------------------------------------------------ \r\n")
		if p.find('.sql') > -1:	
			file.write( ' osql -Sxxxx -Uxx -Pxxx -d '+lib+' -i ".'+p+ '" -r -o '+p[1:].replace( "\\","_").replace( ".","_")+".log    \r\n")
	
file.write( " pause  \r\n")
file.close()