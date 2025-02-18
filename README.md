# PracticEngine

Продолжение проекта по ПИ

1) Сначала подключили репозиторий
  git clone https://github.com/Danolexity/PracticEngine.git

2) Создаем ветку и переходим в нее
  git checkout -b "Project_test"

3) После сделанных изменений сохраняем все изменения
  git add .

4) Делаем первый коммит с сообщением "test_commit"
  git commit -m "test_commit"

5) Делаем первый пуш (Push)
    git push origin

6) Выдает ошибку, т.к. ветка не Project_test не имеет вышестоящей ветки, поэтому предлагается решение
    git push --set-upstream origin Project_test

7) Перейдем в ветку main (основную ветку)
    git checkout main

8) Посмотрим последние изменения
    git pull origin main

9) Проведем слияние ветки с изменениями в основную ветку
    git merge Project_test

10) Отправим изменения из освноной ветки в удаленный репозиторий
    git push origin main