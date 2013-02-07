BEGIN;
    INSERT INTO agenda_course (courseNr, name, semester, mode)
    VALUES ( "187.237"
           , "Gesellschaftliche Spannungsfelder der Informatik"
           , "2013S"
           , "VU");
    INSERT INTO agenda_course (courseNr, name, semester, mode)
    VALUES ("185.278"
           , "Theoretische Informatik und Logik"
           , "2013S"
           , "VU");
COMMIT;