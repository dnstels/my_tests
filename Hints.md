# Полезные для работы подсказки

## Git

Чтобы просмотреть неотправленные коммиты в Git, можно использовать команду:
`git log --branches --not --remotes`

Для отправления изменений в удаленный репозиторий:
`git push origin main`

Чтобы 'спрятать' изменения используется команда `stash`, перед этим необходимо зафиксировать изменения
(внести в индекс)с помощью команд `add` `rm` `mv`

```shell
git add -A
git stash -m 'описание коммита'
```

Для просмотра спрятанных изменения можно воспользоваться командой:
`git stash list`

Для восстановления спрятанных изменений:
`git stash apply`

или с удалением спрятанных изменений:
`git stash pop`

Удалить спрятанные изменения:
`git stash drop <имя удаляемых изменений>` -> `git stash drop stash@{0}`

## Python

Создать виртуальное окружение
`[path_to\py]python -m venv .venv`

Узнать путь до программы python
Windows:
`Get-Command python`
Linux:
`which python`

Использовать pip:
`python -m pip <опции pip>`

### Pip

Зафиксировать зависимости в файле:
`pip freeze > requirements.txt`

Восстановить зависимости:
`pip install -r requirements.txt`

### pytest

Запуск определенных тестов:
`pytest [options] [filename[::function_name]]`
