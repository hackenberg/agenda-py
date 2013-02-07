BEGIN;
    INSERT INTO agenda_course (courseNr, name, semester)
    VALUES ( "187.237"
           , "Gesellschaftliche Spannungsfelder der Informatik"
           , "2013S");
    INSERT INTO agenda_course (courseNr, name, semester)
    VALUES ("185.278"
           , "Theoretische Informatik und Logik"
           , "2013S");
COMMIT;
