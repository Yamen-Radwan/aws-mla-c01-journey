# Lesson 1: Python Basics



## Why Python matters on AWS

Python is the main language for ML on AWS. It's used in:

- \*\*SageMaker AI training scripts\*\*: the code that trains models

- \*\*AWS Lambda functions\*\*: small pieces of code AWS runs on demand

- \*\*AWS Glue jobs\*\*: data-processing jobs

- \*\*Boto3\*\*: Python's toolkit for controlling AWS services



## Core ideas

| On AWS | Lists of files, instances, records | JSON-style API requests and responses |





### Classes (OOP)

- A class is a blueprint; an object is something built from it.

- ML libraries follow the \*\*fit / predict\*\* pattern: `fit` learns from data, `predict` uses what was learned.

- `fit` ends with `return self`, so calls can be chained: `Model().fit(data).predict(x)`.

- scikit-learn, PyTorch, and the SageMaker Python SDK (`fit`, `deploy`, `predict`) all use this style.



### Error handling

- `try`: code that might fail. `except`: handles specific errors. `finally`: always runs.

- Put specific exceptions before the general `Exception`.

- Failed Boto3 calls (missing permissions, throttling) raise `botocore.exceptions.ClientError`.



### File I/O

- `with open(...) as file:` closes the file automatically, even after errors (a context manager).

- Modes: `'r'` read, `'w'` write (\*\*erases existing content\*\*), `'a'` append.

- On AWS, data usually lives in S3, not local disk. Pandas can read `s3://` paths (needs `s3fs`), and Boto3 can upload and download objects.



## Exam angle

The exam doesn't test Python syntax. It tests the tools you use Python with:



| Tool | What it is | Use it when |

|---|---|---|

| Console | AWS website, point and click | Learning, exploring, one-off tasks |

| AWS CLI | Typed commands in a terminal | Quick scripts, automation |

| Boto3 | Python library covering most AWS services | Programmatic control from Python |

| SageMaker Python SDK | Higher-level library focused on SageMaker | Training, deploying, managing models |



- Expect scenarios about deploying and hosting models programmatically (SDK, Boto3, or CLI).

- Modular, reusable code is a tested software engineering best practice.



## Lab: threshold\_pipeline.py

Built a small ML-style program using a class (`SimpleThresholdModel` with fit and predict), file reading and writing, and try/except/finally.

- Learned threshold from the training data

- Wrote predictions to `results.txt`

- Broke it on purpose (moved the data file) to trigger `FileNotFoundError`; `finally` still ran.



## My notes and questions

N/A for now.. Thank you for following along if you are here :)