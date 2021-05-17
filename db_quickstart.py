from database import Database

db = Database('test_case_magic.db')
db.create_table('cases', '(case_id INTEGER PRIMARY KEY, name text, steps blob)')
db.create_table('suites', '(suite_id INTEGER PRIMARY KEY, name text)')
case_suite_relations_schema = '''
    (
        case_id INTEGER,
        suite_id INTEGER,
        suite_case_order INTEGER,
        UNIQUE(case_id, suite_id),
        FOREIGN KEY(case_id) REFERENCES cases(case_id),
        FOREIGN KEY(suite_id) REFERENCES suites(suite_id)
    )
'''
db.create_table('case_suite_relations', case_suite_relations_schema)