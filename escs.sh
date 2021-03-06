##############################################################################
# Push django-onesignal staging branch.
cd ~/projects/django-onesignal-code
# clean up all .pyc files. 
find . -name "*.pyc" -exec rm -f {} \;
git status
git add *
git commit -a
git push -u origin staging
#############################################################################
# Push django-onesignal on master.
cd ~/projects/django-onesignal-code
# clean up all .pyc files. 
find . -name "*.pyc" -exec rm -f {} \;

git status
git add *
git commit -a
git push -u origin master
##############################################################################
# Merge staging into master.
git checkout master
git merge staging
git push -u origin master
git checkout staging
##############################################################################
# Merge master into staging.
git checkout staging
git merge master
git push -u origin staging
git checkout staging
##############################################################################
# Create staging branch.
cd ~/projects/django-onesignal-code
git branch -a
git checkout -b staging
git push --set-upstream origin staging
##############################################################################
# create releases.

git tag -a v1.0.0 -m 'Initial release'
git push origin : v1.0.0

git tag -a v2.0.0 -m 'Running on django 2.'
git push origin : v2.0.0
##############################################################################
# Upload the package.
python setup.py sdist register upload
rm -fr dist
##############################################################################
# Create demo project.

cd ~/projects/
django-admin startproject demo django-onesignal-code
##############################################################################
# Make migrations for the app.
cd ~/projects/django-onesignal-code

python manage.py makemigrations onesignal
#####k#########################################################################
# create django-onesignal virtualenv.
cd ~/.virtualenvs/
ls -la
virtualenv django-onesignal -p python
##############################################################################
# Install requirements.
cd ~/projects/django-onesignal-code

pip install -r requirements.txt 
#####k#########################################################################
# activate django-onesignal virtualenv.

cd ~/.virtualenvs/
source django-onesignal/bin/activate
cd ~/projects/django-onesignal-code

