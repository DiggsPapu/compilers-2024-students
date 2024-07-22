grammar ConfRoomScheduler;

prog: stat+ ;

stat: reserve NEWLINE                # reserveStat
    | cancel NEWLINE                 # cancelStat
    | reschedule NEWLINE             # rescheduleStat
    | NEWLINE                        # blank
    | 'LIST'                         # listStat
    ;

reserve: 'RESERVAR' roomType ID 'PARA' ID 'PARA' DATE 'DE' TIME 'A' TIME (description)?; 

cancel: 'CANCELAR' roomType ID 'PARA' ID 'PARA' DATE 'DE' TIME 'A' TIME ; 

reschedule: 'REPROGRAMAR' roomType ID 'PARA' ID 'PARA' DATE 'DE' TIME 'A' TIME 'A' DATE 'DE' TIME 'A' TIME ;

description: 'DESCRIPCION:' (ID)+;

roomType: 'JUNTAS' | 'CAPACITACION' ;  // Add other types as needed

DATE: DIGIT DIGIT '/' DIGIT DIGIT '/' DIGIT DIGIT DIGIT DIGIT ;
TIME: DIGIT DIGIT ':' DIGIT DIGIT ;
ID  : [a-zA-Z0-9]+ ;
NEWLINE: '\r'? '\n' ;
WS  : [ \t]+ -> skip ;

fragment DIGIT : [0-9] ;
