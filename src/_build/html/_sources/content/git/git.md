# A guide for git

Sources: <https://youtu.be/HVsySz-h9r4>

## Help

<div class="highlight-bash notranslate"><div class="highlight"><pre>git help <i>VERB</i>
git <i>VERB</i> -- help</pre></div>
</div>
examples:
    
```bash
git help config
git config --help
```

## Setup

* check version

    ```bash
    git --version
    ```
* setup name and email
  <pre><code lang="bash">git config --global user.name "<i>NAME</i>"
  git config --global user.email "<i>EMAIL</i>"</code></pre>

* check config
  ```bash
  git config --global --list
  ```
* initialize git repository from existing local project
  ```bash
  git init
  ```
* initialize git repository from remote project
  <pre><code lang="bash">git clone <i>URL</i> <i>TARGET_DIRECTORY</i></code></pre>

* remove `.git` folder ⇒ remove git from the project 
* to exclude files from version control, use the `.gitignore` file
  <pre><code lang="bash">.idea <i>(FOLDER)</i>
  __init__.py <i>(file)</i>
  *.py <i>(file with wildcard)</i></code></pre>

## Commit

![staging_area](images/stagingarea.png)

* Check status of all changed files
  <pre><code lang="bash">git status</code></pre>

* Check changes in more detail
  <pre><code lang="bash">git diff</code></pre>

* Add file to the staging area
  <pre><code lang="bash">git add <i>FILENAME</i></code></pre>

* Add all changed files to the staging area
  <pre><code lang="bash">git add -A</code></pre>

* Commit (for good documentation, add a very detailed message)
  <pre><code lang="bash">git commit -m "<i>MESSAGE</i>"</code></pre>

## Remote repository

* Get repository information
  <pre><code lang="bash">git remote -v</code></pre>

* List branches (locally/remotely)
  <pre><code lang="bash">git branch -a</code></pre>

* Get code from remote repository
  <pre><code lang="bash">git pull origin BRANCH</code></pre>

* Upload code to remote repository (1st pull because the code could be changed, use -u to associate the local branch with
the remote branch)
  <pre><code lang="bash">git pull origin BRANCH
  git push -u origin BRANCH</code></pre>

## Branching

* Create new branch
  <pre><code lang="bash">git branch <i>BRANCH_NAME</i></code></pre>
* Go to branch
  <pre><code lang="bash">git checkout <i>BRANCH_NAME</i></code></pre>
* Create new branch and go to it
  <pre><code lang="bash">git checkout -b <i>BRANCH_NAME</i></code></pre>
* List local branches *(starred branch is the current branch)*
  <pre><code lang="bash">git branch</code></pre>
* List merged local branches
  <pre><code lang="bash">git branch --merged</code></pre>
* Merge branch into current branch
  <pre><code lang="bash">git merge --no-ff <i>BRANCH_NAME</i></code></pre>
* Delete branch locally
  <pre><code lang="bash">git branch -d <i>BRANCH_NAME</i></code></pre>
* Delete branch remotely
  <pre><code lang="bash">git push origin --delete <i>BRANCH_NAME</i></code></pre>

## Fixing mistakes

* Return to state of the last commit
  <pre><code lang="bash">git checkout <i>CURRENT_BRANCH_NAME</i></code></pre>
* Fix bad commit message
  <pre><code lang="bash">git commit --amend -m "<i>GOOD MESSAGE</i>"</code></pre>
* Add extra file to former commit
  1. add file to the staging area
  2. <pre><code lang="bash">git commit --amend</code></pre>