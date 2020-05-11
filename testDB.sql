SELECT * FROM faces.faceEncoding;
use faces;
update faceEncoding set encoding=null where ID in (1,2,3,4,5,6);
update faceEncoding set encoded=0 where ID in (1,2,3,4,5,6);	# workbench里有安全模式，不支持更新所有行