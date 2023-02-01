
- composer create-project symfony/skeleton proje adı / composer yardımı ile symfony projesi kurma - web yada api diye ayrılmaktadır.
- symfony console / bütün komut listesi
- symfony server:start / projeyi ayağa kaldırma

#### controller
- php bin/console make:controller PostController / controller oluşturma

#### entity - (model) 

-  php bin/console make:entity Post 

#### migration

- symfony console make:migration / entity oluşturduktan sonra migration yaratma
- php bin/console doctrine:migrations:migrate / migration çalıştırma








#### Security-bundle

- composer require symfony/security-bundle / composer paketini yükleme

- symfony console make:registration-form  / kayıt formu oluşturma

- symfony symfony console make:auth / login form için 
