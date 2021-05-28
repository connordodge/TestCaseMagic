# TestCaseMagic QuickStart
To get start quickly you can install all of the depencies inside of a virtual environment using the requirements.txt file

Once you have installed the required packages run the db_quickstart.py file to create the needed database and tables locally. This will create 3 empty sqllite tables whose structure is detailed below.

# Testing
You can run all tests by navigating to the base project folder and running:
`python -m unittest discover tests`

All tests are contained in the tests directory


# TestCaseMagic Database structure
Test Case Magic uses a database with 3 tables to achieve a many to many relationship structure between the cases table and the suites table. 

**cases**
| case_id  | name   | steps |
| -------- | ------ | ----- |
| 1        | name 1 | blob  |
| 2        | name 2 | blob  |
| 3        | name 3 | blob  |

**suites**
| suite_id  | name   | 
| --------- | ------ |
| 1         | name 1 |
| 2         | name 2 |

**case_suite_relations**
| case_id  | suite_id   | suite_case_order |
| -------- | ---------- | ---------------- |
| 1        | 1          | 1                |
| 2        | 1          | 2                |
| 1        | 2          | 2                |
| 3        | 2          | 1                |

The 3rd table, case_suite_relations, contains foreign keys for the case ids and the suite ids. It also contains the order of the case ids in the suite.

The database is implemented using sqllite3.

# API
The Test Case Magic API is implemented using Flask and Flask Restful.

## Case Resource
### /case
#### POST
Posting a new case expects a json object with the following structure
```
{
  "name": "case name",
  "steps": [
        {
            "description": "navigate to /auth",
            "type": "ACTION"
        },
        {
            "description": "username and password fields exist",
            "type": "ASSERTION"
        }
  ]
}
```

This will return a 200 with the following structure:
```
{
  "case_id": <int: case_id>
  "name": "case name",
  "steps": [
        {
            "description": "navigate to /auth",
            "type": "ACTION"
        },
        {
            "description": "username and password fields exist",
            "type": "ASSERTION"
        }
  ]
}
```

### /case/\<int:case_id\>
#### GET
A get request for a valid id will return an object of this form:
```
{
  "case_id": <int: case_id>
  "name": "case name",
  "steps": [
        {
            "description": "navigate to /auth",
            "type": "ACTION"
        },
        {
            "description": "username and password fields exist",
            "type": "ASSERTION"
        }
  ]
}
```

A get request for a non-existent integer id will return a 404.


#### PUT
To update a case of the desired id you need to submit request data of the following form
```
{
  "name": "updated case name",
  "steps": [
        {
            "description": "navigate to /auth",
            "type": "ACTION"
        },
        {
            "description": "username and password fields exist",
            "type": "ASSERTION"
        }
  ]
}
```
The test case with the id specified in the url will have its name and steps set to the submitted name and steps.

## Case Merge
### /case/merge
#### PUT
To merge two cases you must submint a PUT request with request data of the following form:
```
{
    "ordered_case_ids":[1,2],
    "new_name": "merged case"
}
```

The steps from the second case id will be appended to the steps of the first case id.
Any suites that have either the 1st or 2nd case id in them will be updated to have exactly 1 copy of the first case id in them.
The 2nd case will be deleted.

## Suite Resource
### /suite
#### POST
To post a new suite you need to submit request data of the following form
```
{
    "ordered_case_ids":[1,2,3,etc],
    "name": "suite name"
}
```

the request will return
```
{
    "cases": [
        1,
        2,
        3,
        etc
    ],
    "name": "merging suite",
    "suite_id": <int: suite_id>
}
```

### /suite/\<int:suite_id\>
#### GET
```
{
    "cases": [
        1,
        2,
        3,
        etc
    ],
    "name": "merging suite",
    "suite_id": <int: suite_id>
}
```

#### PUT
To update a suite you need to submit request data of the form
```
{
    "ordered_case_ids":[1,2,3,etc],
    "name": "suite name"
}
```

the suite with the id specified in the url will have its name and ordered case ids updated
