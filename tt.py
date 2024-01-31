
"""
{% static '' %}

scp -i ~/django-portfolio-key.pem -r MyResume ubuntu@3.37.197.249:/home/ubuntu
ssh -i ~/django-portfolio-key.pem ubuntu@3.37.197.249
pip install 'django<5' 'pillow<10' 'django-admin-thumbnails<0.3'




git init
git add .
git commit -m ""
git remote add origin https://github.com/usung1/Portfolio.git
git push -u origin main

git pull origin main --allow-unrelated-histories
이 명령어는 서로 다른 히스토리를 갖는 브랜치를 병합할 때 사용됩니다. 이를 사용하면 서로 다른 히스토리를 갖는 브랜치를 병합할 수 있습니다.

git clone https://github.com/usung1/Portfolio.git mynewre



# 현재 브랜치에서 새로운 원격 저장소의 변경사항을 가져옵니다.
git pull origin main

# 가져온 변경사항을 현재 브랜치에 적용합니다.
git merge origin/main --allow-unrelated-histories

# 변경사항을 원격 저장소로 푸시합니다.
git push origin main





# 현재 등록된 원격 저장소 확인
git remote -v

# "origin"이라는 원격 저장소를 제거
git remote remove origin

# 새로운 원격 저장소 추가
git remote add <new-remote-name> <repository-url>
"""