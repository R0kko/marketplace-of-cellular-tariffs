![Логотип (XS)](https://user-images.githubusercontent.com/89997389/144845823-cf417dfe-9699-4223-b428-916bb6df6114.png "Маркетплейс тарифов сотовой связи")
     
**Проект по курсу научно-исследовательского семинара "Введение в облачные технологии компании Microsoft"**

## Описание доменной области
### Введение
Данный документ описывает информацию, а также принципы ее обработки, которые должны быть применены при руководстве разработкой программного обеспечения для автоматизации процесса сравнения, оценки результатов и селекции тарифных планов сотовой связи.


### Глоссарий
* Тариф (тарифный план) — форма коммерческого предложения, в которой указывается перечень возможных услуг и порядок определения их цены.


### Основные сведения о домене
* Большинство тарифов включают в себя совокупность услуг в виде различного количества минут телефонной связи (в России — внутри страны, за исключением республики Крым и города Севастополь), исходящих СМС и гигабайт интернет-трафика, а также дополнительные услуги (подписки на сторонние сервисы), элементы трафика, нерасходующего пакеты услуг, дополнительные минуты для звонков на «городские» (стационарные) номера.
* Каждый тарифный план имеет ассоциированного эмитента — оператора сотовой связи, его предлагающего.
* Некоторые тарифы имеют региональную привязку, то есть могут быть недоступны для жителей других регионов, или предлагаться по отличной от основной цене, указанной в оферте.
* Тарифы, которые невозможно подключить в общем порядке не представляют интереса для потенциального пользователя.
* Часть тарифов изначально созданы для определённого вида устройств, а равно, должны иметь соответствующую отметку.
* Домен может содержать акционные предложения (например, более привлекательную цену по промокоду), а следовательно должен быть ассоциирован с соответствующими условиями.


###  Клиенты и пользователи
* Потенциальными клиентами системы в первом приближении являются розничные клиенты, физические лица, нуждающиеся в приобретении новой сим-карты или смены оператора с сохранением телефонного номера (далее «переход по MNP»)
* Система не требует специального обслуживания в процессе эксплуатации. Системный администратор может корректировать работу и исправлять возникающие ошибки, вручную добавлять тарифные планы. 


### Среда и окружение
Клиенты и администраторы используют как мобильные, так и стационарные устройства, включая, но не ограничиваясь ПК, ноутбуки, смартфоны, планшетные компьютеры. Они работают под различными операционными системами, однако требования к совместимости предъявляются только в отношении Windows 10 и новее и MacOS Monterey 12.0.1 и новее. 


### Задачи и процедуры, реализуемые в настоящее время
* Фильтрация тарифных планов по критериям, указываемых пользователем. 
Состав фильтров и их чувствительность в настоящее время уточняется.
Проверяется допустимость отклонения от входных значений с целью представить наиболее выгодное предложение. Аналогично анализируется наполнение фильтров «по типу устройства».
* Подписка на изменения цены по отслеживаемым тарифам. 
Нет подтверждения актуальности данного сервиса в связи с падением ценности этой информации после приобретения сим-карты, например, другого оператора.


### Конкурентное ПО
С данным типом доменов уже работает ряд компаний как на территории России, так и за рубежом. Отечественные сервисы предалагают либо неактуальную информацию, либо плохо визуализированы, не учитывают все условия тарифных планов. Зарубежные конкуренты в основном интегрированы в системы продаж мобильных устройств, подразумевая покупку телефона с программно заблокированной сим-картой одного оператора. Подобные предложения отсутствуют на территории России. 
В данном домене возможен ручной выбор тарифа пользователем, без необходимости обращения к программному обеспечению.


### Сходство с другими доменными областями
Подобная работа по селекции аналогична множеству маркетплейсов по продаже физических товаров и лишь отвечает потребностям клиентов в новой сфере экономики.

## Use-cases

### 1. Запуск веб-приложения
**Описание:** Пользователь подключается к серверу и запускает веб-приложение.

**Предусловия:** Пользователь имеет доступ к интернету и браузер, встроенный в операционную систему, поддерживающий отображение изображений и javascript.

**Результат:** Веб-приложение готово к использованию.

**Триггер:** Пользователь переходит по ссылке с веб-приложением.

**Успешный сценарий:**

1. Пользователь переходит по ссылке, указывающей на серевер с веб-приложением.
2. Веб-приложение запускается, перед пользователем отображется заглавная страница сайте.
3. На заглавной странице отображена основная информация о сервисе и ряд основных тарифных планов, распостроняемых на коммерческой основе (либо наиболее популярных среди пользователей).

### 2. Использование фильтров
**Описание:** Пользователь использует окно с выбором фильтров для подбора оптимального тарифного плана под собственные задачи.

**Предусловия:** Пользователь подключен к веб-приложению и его инициализация (case №1) полностью выполнена.

**Результат:** Приложение фильтрует базу данных тарифных планов и визуализирует для пользователя подходящие блоки информации.

**Триггер:** пользователь взаимодействует с кнопкой "подобрать тариф".

**Успешный сценарий:**

1. При нажатии на кнопку "Подобрать тариф" отображается структурированое меню, состоящее из различных полей, которые пользователь выборочно заполняет, в зависимости от потребностей.
2. При нажатии кнопки применить, после заполнения полей, проверяется корректность входных данных. В случае ошибки, необходимо вернуться у шагу №1 этого же кейса.
3. При корректности входных данных система проводит фильтрацию БД тарифных планов, данные из подходящих строк визуализируются и представляются пользователю в виде списка кликабельных блоков.

### 3. Просмотр подробной информации о тарифе.
**Описание:** Пользователя заинтресовал тарифный план и у него есть желание узнать подробные условия предложения.

**Предусловия:** Пользователь подключен к веб-приложению и его инициализация (case №1) полностью выполнена и/или пользователь применил фильтры (case #2).

**Результат:** Пользователь видит типовой лендинг с информацией о тарифном плане, подробными условиями и ссылкой на сайт для оформления покупки.

**Триггер:** пользователь взаимодействует с кнопкой "Подробнее" в блоке визуализации тарифного плана.

1. При нажатии на кнопку "Подробнее" веб-приложение загружает из базы данных всю имеющуюся информацию о предложении. Данная информация заполняет типовую лендинг-страницу, на которую происходит редирект.
2. Пользователь изучает информацию о тарифном плане и, если он ему подходит, нажимает кнопку "Купить". Данная кнопка производит перенаправление пользователя на сайт партнера по реферальному взаимодействию, а тот в свою очередь на сайт сотового оператора. На этом взаимодействие пользователя и сервиса завершается, веб-приложение отображает сообщение с благодарностью за использование сервиса и кнопкой перенаправления на заглавную страницу (сase #1) Нажатие кнопки "Сохранить в избранное" проверяет авторизацию пользователя и, если тот авторизован записывает данный тарифный план в персональный раздел сайта.
3. Если тарифный план пользователю не подходит, предусмотрено возвращения к п. 3 case #2 с сохранением ранее примененных фильтров нажатием кнопки "назад".

### 4. Регистрация личного кабинета пользователя
**Описание:** Пользователь взаимодействует с персонализированными функциями сайта и получил предложение зарегистрировать личный кабинет.

**Предусловия:** Пользователь подключен к веб-приложению и его инициализация (case №1) полностью выполнена и пользователь был перенаправлен на этот use-case другим компонентом, работа которого невозможна без ЛК.

**Результат:** Пользователь зарегестрирован и авторизован в личном кабинете и получил доступ к персональному разделу сайта.

**Триггер:** Установлена необходимость регистрации пользователя в Use-case #5 "Авторизация".

**Успешный сценарий:**
1. Отображение окна с формой регистрации, содержащей поля "имя", "фамилия", "отчество", "дата рождения", email, "телефон", согласие на обработку персональных данных (152-ФЗ). Переход к шагу 2 после заполнения всех полей пользователем и нажатим кнопки "регистрация".
2. Проверка корректности заполненных данных, в случае корректного заполнения - сохранение в БД и переход к шагу 3. Иначе - сообщение об ошибке с указанием некорректно заполненных полей и возврат к шагу №1 с сохранением на пользовательском устройстве ранее введенной информации. 
3. На указанный email отправляется 5-значный код, на экране пользователя отображается поле для его ввода. При корректном вводе кода - переход к следующему шагу, иначе - отображение сообщения об ошибке, появления блока "отправить новый код" (доступный только после ввода каптчи). Нажатие на этот блок отправляет новый код на указанный адрес и повторяет шаг №3.
4. Отображение сообщения об успешной регистрации, авторизация текущей пользовательской сессии.

### 5. Авторизация в личном кабинете пользователя
**Описание:** Пользователь пытался взаимодействовать с персонализированными функциями сайта и не был авторизован ранее. Производится вход в личный кабинет пользователя.

**Предусловия:** Пользователь подключен к веб-приложению и его инициализация (case №1) полностью выполнена и пользователь был перенаправлен на этот use-case другим компонентом, работа которого невозможна без ЛК.

**Результат:** Пользователь авторизован в личном кабинете и получил доступ к персональному разделу сайта или перенаправлен в раздел регистрации.

**Триггер:** Установлена необходимость авторизации пользователя или нажата кнопка "Авторизация".

**Успешный сценарий:**
1. На экране в том же окне отображается форма авторизации, содержащая два поля: "email" и "пароль". Пользователь вводит свои учетные данные и нажимает кнопку "войти". 
2. Происходит проверка учетных данных. Если данные корректны, происходит авторизация сессии работы с приложением, пользователь получает доступ к персональному разделу сайта. Иначе переход к п.3.
3. Отображается сообщение об ошибке в верхней части экрана о неверно введенных учетных данных. Возле кнопки войти появляется блок "Сбросить пароль". Если пользователь вносит изменения в ранее веденные данные и нажимает кнопку "войти", переход к п. 3. Если пользователь выбирает "Сбросить пароль" переход к п. 4. Если "Регистрация" - к use-case #4.
4. Отображается окно с одним полем "email". При вводе пользователем email проверяется его корректность, переходим к шагу №5. Иначе отображается сообщение об ошибке и кнопка регистрация, нажатие на которую переводит на use-case #4.
5. На указанный email отправляется 5-значный код, на экране пользователя отображается поле для его ввода. При корректном вводе кода - переход к следующему шагу, иначе - отображение сообщения об ошибке, появления блока "отправить новый код" (доступный только после ввода каптчи). Нажатие на этот блок отправляет новый код на указанный адрес и повторяет шаг №5.
6. Отображение поля "новый пароль". Пользователь указывает новый пароль, проверяется его соответствие минимальным требованиям. В случае корректности - сохранение нового пароля, авторизация текущей сессии. Иначе, отображение сообщения об ошибке и минимальных требованиях к паролю, повторение вызова шага №6.

### 6. Работа с личным разделом сайта.
**Описание:** Пользователь обращается к личному разделу сайта для просмотра/изменения сведений.

**Предусловия:** Пользователь подключен к веб-приложению и его инициализация (case №1) полностью выполнена и пользователь перешел в личный кабинет нажатием кнопки в меню сайта и его сессия предварительно авторизована.

**Результат:** Пользователь ознакамливается с информацией в ЛК/вносит изменения.

**Триггер:** пользователь кликает по иконке "личный кабинет".

1. Отображается страница сайта, состоящая из двух блоков - "личные данные" и "избранные тарифы". Перед формированием списка избранны тарифов проверяется их актуальность (наличие в БД активных предложений). Если все ок - тариф попадает в список - иначе на его месте отображается блок "потреял актуальность".
2. При нажатии на блок тарифа в списке "избранные тарифы" происходит переход к use-case #3 с формированием лендинга для соответствующего тарифа.
3. При внесении изменений в поля личных данных и нажатии кнопки "сохранить" происходит проверка учетных данных. Если данные корректны, происходит авторизация сессии работы с приложением, в БД вносятся изменения. Иначе переход к п.1. Отображается сообщение об ошибке в верхней части экрана о неверно введенных учетных данных. Если внесено изменение в поле email, переход к п.4.
4. На указанный email отправляется 5-значный код, на экране пользователя отображается поле для его ввода. При корректном вводе кода - внесение изменений в БД, иначе - отображение сообщения об ошибке, появления блока "отправить новый код" (доступный только после ввода каптчи). Нажатие на этот блок повторяет шаг №4.

## Описание технических требований
- Нефункциональные требования:
  1. Веб-приложение должно быть доступно для просмотра со смартфонов, планшетов и компьютеров.
  2. Приложение должно использовать базу данных для долгосрочного хранения данных.
  3. ПО не должно аварийно завершаться при любых входных данных, таким образом, должна осуществляться проверка входных данных на корректность.
  4. Интерфес приложения должен быть интуитивно понятен пользователю, все основные элементы должны масштабироваться по ширине и адаптироваться к экрану пользователя.
  5. Инициализация клиентской части приложения должна происходить быстрее 5 секунд.

- Функциональные требования:
  1. Приложение должно хранить в базах данных информацию о тарифных планах.
  2. Данная информация может быть загружена в архитектуру приложения как вручную, так и с использованием средств автоматической обработки информации.
  3. ПО должно сортировать и фильтровать тарифные планы, содержащиеся в БД, по указанным пользователем условиям, представлять их пользователю. Обработка и применение фильтров должно происходить быстрее трех секунд. 
  В каждом из окон, отражающих общую информацию о тарифе, должно содержаться название оператора, количество минут/смс/гигабайт, включенных в указанную стоимость. Должна быть рассчитана общая оценка тарифа, отражающая уровень привлекательности предложения относительно других. Не допускается отображение тарифного плана без прямого указания стоимости услуг.
  4. По каждому тарифному плану должна содержаться подробная информация из публичной оферты компании-оператора, ссылка, ведущая на сайт партнера, ответственного 
за монетизацию формируемого трафика и, в дальнейшем, на форму заказа сим-карты на сайте эмитента.
  6. В перспективе, выходящей за рамки исследовательского семинара, требуется предумотреть возможность организации персонального раздела сайта ("личного кабинета") и интеграции в ЕСИА "Госуслуги" по API.

## Компонентная модель
<img width="1359" alt="Снимок экрана 2021-12-07 в 00 27 37" src="https://user-images.githubusercontent.com/89997389/144925387-f2c97c26-5426-432e-8d79-8601898cecb4.png">

## Quickstart for Ubuntu
```bash
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## DockerHub
```bash
docker pull 4svon/market_place_of_ct
docker run -p 8000:8000 market_place_of_ct:main
```