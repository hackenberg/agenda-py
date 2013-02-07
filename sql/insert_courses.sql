BEGIN;
    INSERT INTO agenda_course (courseNr, name, semester, mode, ects)
    VALUES ("182.709"
           , "Betriebssysteme"
           , "2013S"
           , "UE"
           , 4);
    INSERT INTO agenda_course (courseNr, name, semester, mode, ects)
    VALUES ( "187.237"
           , "Gesellschaftliche Spannungsfelder der Informatik"
           , "2013S"
           , "VU"
           , 3);
    INSERT INTO agenda_course (courseNr, name, semester, mode, ects)
    VALUES ("185.278"
           , "Theoretische Informatik und Logik"
           , "2013S"
           , "VU"
           , 6);
COMMIT;