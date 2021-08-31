
## TryDjango from freecodecamp.org 
From youtube freecodecamp channel:  [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/channel/UCWEHue8kksIaktO8KTTN_zg)

This django project is a step-by-step practice, the source code is from [CodingforEntrepreneurs](https://github.com/codingforentrepreneurs/Try-Django).It introduces much common practice of Django Framework.The customized apps in the project include:
- pages.   This app aims to quickly go through from the url pattern to view controller,introducing some common settings running a app(service).

## Git command lines to conect the local repository to remote repository.
### create a new repository on the command line
```
echo "# trydjango" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/smallmacro/trydjango.git
git push -u origin main
```

### push an existing repository from the command line
```
git remote add origin https://github.com/smallmacro/trydjango.git
git branch -M main
git push -u origin main
```
### import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.
