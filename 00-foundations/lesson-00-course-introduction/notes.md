# Lesson 0: Course Introduction



## Course-to-exam map

- Course 1 → Domain 1: Data preparation for ML

- Course 2 → Domain 2: ML model development

- Course 3 → Domain 3: Deployment and orchestration

- Course 4 → Domain 4: Monitoring, maintenance, and security



## Key idea

Building a model once is a proof of concept; production ML must be reliable, secure, monitored, and cost-efficient.



## Vocabulary

- MLOps: Applying DevOps habits (automation, testing, versioning) to ML

- Model drift: accuracy decays as real-world data changes

- Feature store: A shared, versioned library of ready-to-use input variables

- Data lineage: A record of where data came from and how it was changed

- Model registry: A catalog of model versions with approvals

- Blue-green deployment: new and old versions run side by side; switch traffic, roll back instantly (Similar to Opening a new restaurant branch while the old one stays open)

- SLA: promised performance level (e.g., “responds within 200 ms”) short for Service Level Agreement (SLA)



## AWS Exam mindset

Questions are scenarios about trade-offs between cost, performance, security, and reliability.

## The big idea: from experiment to production

Think of a restaurant. Training a model in a notebook is like cooking a great dish once in your home kitchen. Production ML is running a restaurant: serving that dish to thousands of people every day, consistently, safely, within budget, and noticing when quality drops. The course (and the exam) is about the restaurant, not the home kitchen.


