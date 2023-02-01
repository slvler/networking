
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


#### Doctrine

      
        // findbyall - select * from tablo
        // find - select * from tablo where id = 5;
        // findby - select * from tablo order by id desc
        // findoneBy - Select * from tablo where id = 6 and title = "title" order by id desc




# Bundle Alanı


#### Security-bundle - auth registir login logout olaylarını ve servis katmanını kullanabilmek için

- composer require symfony/security-bundle / composer paketini yükleme

- symfony console make:registration-form  / kayıt formu oluşturma

- symfony symfony console make:auth / login form için 


#### Annotations - annotations özelliğini kullanabilmek için
- composer required annotations / composer paketini yükleme



#### Maker - make komutunu kullanabilmek için
- composer require maker


#### Orm - Orm mimarısını kullanabilmek için
- composer require symfony/orm-pack



#### Doctrine fixtures bundle - Seeder Factory işlemleri için
-  composer require --dev doctrine/doctrine-fixtures-bundle

