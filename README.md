Асинхронный код.


## .ENV
Файл `.env` разместите в корне проекта 
```text
PROJECT_REFERRAL_SETTING_POSTGRES_DB=< db-name >
PROJECT_REFERRAL_SETTING_POSTGRES_USER=< user-name-from db >
PROJECT_REFERRAL_SETTING_POSTGRES_PASSWORD=<password-from-db>
PROJECT_REFERRAL_SETTING_POSTGRES_HOST=< host-of-db >
PROJECT_REFERRAL_SETTING_POSTGRES_PORT=< port-of-db >
PROJECT_REFERRAL_SECRET_KEY=< flask-secret-key >
MAIL_SERVER=smtp.mail.ru
EMAIL_PORT=25
MAIL_USE_TLS=True
MAIL_USERNAME=< email-from-admin-site >
MAIL_DEFAULT_SENDER=< your@mail.zone > 
MAIL_PASSWORD=< pasword-from-your-email >
TOKEN_TIME_MINUTE_EXPIRE=2

```
## Commands
Базовые команды от Flask и IDE.



###  Команды из fronted
[referral_frontend](https://github.com/Tryd0g0lik/referral_frontend).\
В качестве сборщика выступает '`yarn`'. Если работаете \
с '`npm`' - удалить `'yarn.lock'` \
```text
// Установка зависимостей
`npm run install` или `npm run install package.json`


// Запустить проверки стиля для написанного кода
`run npm lint`

// Развернуть файлы (frontend) в режиме сборки
`npm run build:front`

// Для работы с проектом запустить сервер (frontend)
`npm run server:front`

```

#### build:front
Сборка файлов проводится в директории:
- `referral\templates`;
- `referral\static` из '`referral`'

Note: Для работы с JS `[JS-файлами](src/sripts)

Файлы JS имеют динамические имена. Перед размещением новых файлов, \
предыдущие удаляются автоматически.

## Dependence
Удалите файл `pyproject.toml` если в качестве установщика используете `pip`. \
Проект собирался на установщике `Poetry`\
[requirements.txt](requirements.txt) продукт авто-сборки от `Poetry`.

## Descript

Зaпуск модуля открывает стартовую страницу  

![main.png](img/main.png)

### Меню
Меню:
- "Главная" - страница открывается при запуске модуля.
- "Регистрация" и "Вход" - ссылку в меню видим в не авторизованном режиме.
- "Профиль" и подменю от "Профиль" видим в авторизованном режиме 

### Отсутствует
Проект не имеет:
- деактивации по истечении времени;
- Кеширование не везде;
-  UI - тест.

### Валидация
Поля формы имеют базовую валидацию и дополнительную на \
стороне '`views-файлов`'. \
Например: \
```text
# Check a field empty
if not password:
    return render_template(
        "users/register.html",
        form=form,
        message="Password cannot be empty.",
    
    )

if password != password2:
    return render_template(
        "users/register.html",
        form=form,
        message="Passwords do not match.",
    )
```

### JS из репо referral_frontend/frontend 
JS файлы имеют динамические имена. Удобно для отслеживания версий. \
Размещаются в дереве на этапе сборки '`webpack`' из \
[referral_frontend](https://github.com/Tryd0g0lik/referral_frontend).

### Регистрация
**views.py**:
- `referral/views_more/views_account.py`;
- 120 секунда для подтверждения email.
- Если не успели или не нашли на почте ссылку из ресурса, возможно использовать
кнопку "Повторить токен". Указать Email для отправки ссылки.

### Авторизация
**Первичная авторизация**:
 - Отправляем 'GET' на сервер и получаем '`csfr_token`' после \
запрашиваем '`user_token`'.
 - сохраняем его '`Cookie`'. Далее ориентируемся на \
логин '`user_token`' вместо. 
'email'. 
 

Клик по ссылке "Регистрация" видим форму для регистрации \
![register.png](img/register.png)



### Вход
**views.py**:
- `referral/views_more/views_account.py`.

Клик по ссылке "Вход" видим форму для авторизации \
![loginin.png](img/loginin.png)

Note: "Повторить токен" в данный момент кнопка не рабочая. Может привести к \
ошибке.
#### Повторить токен
**views.py**:
- `referral/views_more/views_account.py`.


Проект имеет отдельный репозиторий для '`frontend`'. 
Через '`TypeScryot`' планируется сделать функционал. При клике, попадаем на \
страницу '`/repeat_token`'. 

В данный момент руками , вставляем в браузер '`/repeat_token`' и получаем \
форму для повторной отправки токена на указанный '`Email`'. \
![token_repeat.png](img/token_repeat.png)

### Токен поступивший на почту
Сейчас лучше скопировать ссылку и самим вставить в адресную сроку браузера.\
Пользователя перекидывает на страницу с формой для авторизайии.\
Если ссылку сами вставили в адресную сроку браузера мене чем 120 секунд после \
регистрации, значит авторизация пройдет успешно.

Если не успели, наберите адрес '`/repeat_token`' и укажите '`Email`' для \
повторной отправке.

### Профиль
- cсылку видно в меню после авторизации;
- наводим курсор на профиль и появляется подменю.\
![dashboard.png](img/dashboard.png)

#### Добавить код
При клике видим форму для создания реферального кода.\
![referral_code.png](img/referral_code.png)

Note: В данный момент не рабочая.

### Пароль для авторизации
В DB сохраняется в хешированом виде. \
Хешировать Email или нет надо уточнять.

### DB
**models.py**:
- `referral/models_more/model_init.py`;
- `referral/models_more/model_users.py`;
- `referral/models_more/model_referral.py`.

#### DB '`Users``' имеет следующее
- '`firstname`' - имя пользователя;
- '`email`' - email пользователя. Он должен быть уникальный. Часть логики \
backend ориентируется на него;
- '`password`'  пароль;
- '`send`' - по умолчанию '`False`'. '`True`' - сообщения для аутентификации \
отправлено на почту.
- '`is_activated`' - По умолчанию '`False`'. '`True`' - клик по ссылке \
прошел в течении 120 секунд. Как итог пользователь перебрасывается на страницу \
[для авторизации](#вход). Успешное событие , из db удаляет \
время ('`token_created_at`') создания токена. Сам токен остается. Часть \
логики на него ориентируется;
- '`is_active`' - По умолчанию '`False`'. '`True`' - сообщения \
для аутентификации  отправлено на почту;
- '`date`' - время регистрации пользователя;
- '`activation_token`' - токен;
- '`token_created_at`' - время создания токена. Первые 120 секунд токен \
сохраняет рабочее состояние.

#### DB '`Referrals``' имеет следующее
- '`user_id`' - index пользователя из db '`Users`';
- '`referral_code`' - реферальный код;
- '`is_send`' -  по умолчанию '`False`'. '`True`' - сообщения для \
отправлено на почту;
- '`is_activated`' - по умолчанию '`False`'. '`True`' - код активный; 
- '`date`' - время создания токена.

![db.png](img/db.png)

### Frontend
В корне '`referral`' создайте директорию '`frontend`' и \
в него скопируете данный репо.
