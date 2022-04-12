# CI/CD Implementation Tests and Documentation Repo

### Software Development Cycle
- [Software Development Documentation](https://docs.google.com/document/d/1vbmhxodqEOuSb-so2PWHQrD098zXapY3rJraD5UeKio/edit)
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
      - `Only on pull request to branches: [feature-test, develop, staging, acceptance] - Linters, Test and Coverage will be triggered`

    - On github.event: push
      - `Only on push/merge to branches: [feature-test, develop, staging, acceptance] - Build and Deploy will be triggered`
      
  - **Production environments**
    - On github.event: pull_request
      - `Only on pull request to branches: [main] - Linters, Test and Coverage will be triggered`

    - On github.event: push
      - `Only on push/merge to branches: [main] - Manual trigger of Build and Deploy`

_Note: reusable workflows are on main branch (default). See [linters-workflow.yml](https://github.com/viyahe/continuous-platform/blob/main/.github/workflows/linters-workflow.yml), [test-workflow.yml](https://github.com/viyahe/continuous-platform/blob/main/.github/workflows/test-workflow.yml) and [deployment-workflow.yml](https://github.com/viyahe/continuous-platform/blob/main/.github/workflows/deployment-workflow.yml) for reference. 

Reference: [Reusing worklows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

_Check [main-workflow.yml](https://github.com/viyahe/continuous-platform/blob/main/.github/workflows/main-workflow.yml) for usage._

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
