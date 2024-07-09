## Understanding git hooks deep dive

### What are git hooks?
Git hooks are simply executable scripts that Git executes before or after events such as: commit, push, and receive. 
Git hooks are a built-in feature - no need to install anything. They are located in the `.git/hooks` directory of every Git repository.


### Normal Git workflow without hooks
By default git allows you to commit any files, enter any commit message and doesn't perform any checks.
```mermaid
flowchart LR
    A[Stage Files] --> B(Commit)
    B --> C(Commit Message)
    C --> D[Committed]
```
 ![img.png](img.png)
 
### Use case of git hooks?
Verify or edit commit message.
Run application tests before each commit or before pushing to remote.
Verify & potentially fix code syntax mistakes using linters like ESlist, Pylint etc.
Generate notification after successful committing.
Deployed updated application to production on the server.