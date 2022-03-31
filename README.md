# CI/CD Implementation Tests and Documentation Repo
### Pre-requisites 

- [Environment Variables](https://docs.google.com/spreadsheets/d/1sWs-Nfzx3ReiiCzKCe7OY5GnQrAiVt_PCasFb9frzpY/edit#gid=1807969178)
  - SSH Key
  - Code Climate IDs
  - AWS Credentials
  - Others (Deployment and Platform)
 
- [Dependencies](https://github.com/viyahe/appsync#requirements)
  - Python > 3.8.0
  - Pipenv
  - Node.js
  - aws-cdk

### Build

```
Define all project dependencies on Pipfile with all corresponding versions.

Check Pipfile on CI/CD documentation repository for examples.

Make use of pipenv to run all linters and tests to optimize workflow run time. See [scripts section on Pipfile]
```

### Workflow Summary
- **Workflow Triggers**
  - **Edge and Staging environments**
    - On github.event: pull_request
      - `Only on pull request to branches: [develop, staging] - Linters, Test and Coverage will be triggered`

    - On github.event: push
      - `Only on push/merge to branches: [develop, staging] - Build and Deploy will be triggered`
      
  - **Production environments**
    - On github.event: pull_request
      - `Only on pull request to branches: [main] - Linters, Test and Coverage will be triggered`

    - On github.event: push
      - `Only on push/merge to branches: [main] - Manual trigger of Build and Deploy`

_Note: almost several steps are duplicated due to a fresh runner being required for starting each job. For example, the setup of python and ssh key from Linters cannot be used in Test and Coverage because it will instantiate a new OS (Ubuntu 18.04)._

_Check [ci-deployment.yml](#) for reference._

- **Linters**
  - Build from runner (Github OS runner: Ubuntu 18.04)
    1.  Setup python
    2. Set SSH key for cloning dependencies
    3. Install pipenv
    4. Cache dependencies to decrease run time
    5. Install dependencies via pipenv install –dev –deploy
    6. Run all linters via pipenv run `<linters>`
    
- **Test and Coverage**
  - Build from runner (Github OS runner: Ubuntu 18.04)
    1. Setup python
    2. Set SSH key for cloning dependencies
    3. Install pipenv
    4. Cache dependencies to decrease run time
    5. Install dependencies via pipenv install –dev –deploy
    6. Run pytest via pipenv run `<tests>`
    7. Publish code coverage via code climate actions
    
- **Build and Deploy**
  - Needs both Linters, Test and Coverage to be successful
   - Build from runner (Github OS runner: Ubuntu 18.04)
      1. Setup python
      2. Set SSH key for cloning dependencies
      3. Setup node.js
      4. Install aws-cdk
      5. Install pipenv
      6. Cache dependencies to decrease run time
      7. Install dependencies via pipenv install –dev –deploy
      8. Deploy to AWS - pipenv run cdk deploy `<args> <context>`
