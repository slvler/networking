
- composer create-project symfony/skeleton proje adı / composer yardımı ile symfony projesi kurma - web yada api diye ayrılmaktadır.
- symfony console / bütün komut listesi
- symfony server:start / projeyi ayağa kaldırma
- symfony check:requirements / symfony gerekliliklerini denetliyor

#### controller
- php bin/console make:controller PostController / controller oluşturma

#### entity - (model) 

-  php bin/console make:entity Post 

#### migration

- symfony console make:migration / entity oluşturduktan sonra migration yaratma
- php bin/console doctrine:migrations:migrate / migration çalıştırma





# Bundle Alanı


#### Security-bundle - auth registir login logout olaylarını ve servis katmanını kullanabilmek için

- composer require symfony/security-bundle / composer paketini yükleme

- symfony console make:registration-form  / kayıt formu oluşturma

- symfony symfony console make:auth / login form için 


#### Annotations - annotations özelliğini kullanabilmek için
- composer required annotations / composer paketini yükleme



#### Maker - make komutunu kullanabilmek için
- composer require maker

