.. Outpost API documentation master file, created by
   sphinx-quickstart on Fri Sep 20 16:15:01 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GET */*
-------
The standard GET of `api.outpost.travel`_ will return a list of links to our currently avaliable collections. Following these links will result in a list of items. More information on these can be found below in the `/[collection]/` request.

.. code-block:: console

  Request:
  $ curl -i http://api.outpost.travel/

.. code-block:: javascript

  Response:
  {
    _links: {
      child: [
        {
          href: "api.outpost.travel/placeRentals/",
          title: "placeRentals"
        },
        {
          href: "api.outpost.travel/rideShares/",
          title: "rideShares"
        },
        {
          href: "api.outpost.travel/experiences/",
          title: "experiences"
        }
      ]
    }
  }

GET */[collection]/*
--------------------
This GET request requires on of three possible collections. Possible collections are `placeRentals`, `rideShares` and `experiences`. The response will contain two objects, an `_items` array and a `_links` list. The `_items` array contains 25 items which are either places for the `placeRentals` collection, rides for `rideShares` and experiences for `experiences`. The schema is identical for all items in a collection and are quite similar between collections. The `_links` list are to be used for navigation or pseud-pagenation although that is included.

**Options:**

  Pagination:

  `page`:
    `page` is to be used for pagenation as expected. The correct syntax for `page` is `?page=pageNumber`. If the page requested is greater than those avaliable (found in the `_links` list) the response will include an empty `_items` array.
  
  `max_results`:
    `max_results` is to be used with or without pagenation to limit the number or results shown in the `_items` array. The correct syntax for `max_results` is `?max_results=numResults`. The maximum number of results is currently set at 50 results per page and the minimum is 1. If the number is greater or lower than said limits, the page will return 25 results as the default.

  Location based queries:

  `city`:
    `city` can be used to query results that only are for a certain city. `lat` and `lng` will provider a query of the area which may include other municipalites. The proper syntax is `?city=city`. You can then use `sort` (explained later), to sort by `lat` and `lng` or any other key.

  `lat` and `lng`:
    `lat` and `lng` are similar to `city` but query a specific `lat` and `lng`. This will then return all the listings within a radius of a 1-5 kilometers. In the future there will be a option to set the radius via `?radius=1` for 1 kilometer. The proper syntax for `lat` and `lng` is `?lat=lat&lng=lng`.

.. note::
  The following options are subject to change and are not to be used in a production application. They are currently for testing purposes only and will be implemented in the future as full-featured options*

  Sorting:

  `sort`:
    `sort` can be used to sort specific items in ascending order. The syntax is `?sort=itemKey`. Item keys are to be used such as price, city or provider.
  `sortMethod`:
    `sortMethod` is to be used with `sort` to display the results in an ascending or descending order based on the value given. The syntax is `?sortMethod=method` where the method is either `ascending` or `descending`.

All the previous options can be used for both the collections and collection-id GET requests.

.. code-block:: console

  Request:
  $ curl -i http://api.outpost.travel/placeRentals/

.. code-block:: javascript

  Response:
  {
    _items: [
      {
        origin: "La Bordeta, Barcelona, Spain",
        roomType: "shared_room",
        logoLV: "img/airbnb_lv.png",
        hostName: "Isa",
        pid: "145521",
        currency: "USD",
        rate: 33,
        captions: [
          "",
          "",
          "",
          "",
          "",
          "",
          ""
        ],
        propertyType: "apartment",
        logoSV: "img/airbnb_sv.png",
        logoDesc: "Discover amazing, unique accommodations in 192 countries. With more than 10 million nights booked worldwide, Airbnb is the world leader in travel rentals.",
        city: "barcelona",
        houseRules: "Respeto hacia las personas que comparten el piso y con el mobiliario en general.",
        fullProvider: "Airbnb",
        mid: "air145521",
        occupancy: 2,
        etag: "e1931f7e487a1612d8e10805e2b67ffa37a31674",
        amenities: [
          "TV",
          "Internet",
          "Wireless Internet",
          "Air Conditioning",
          "Elevator in Building",
          "Washer",
          "Dryer"
        ],
        provider: "airbnb",
        _links: {
          self: {
            href: "api.outpost.travel/placeRentals/5233838bdb97421b95ab96b6/",
            title: "place"
          }
        },
        thumbnail: "https://a2.muscache.com/pictures/22319501/medium.jpg",
        updated: "Thu, 01 Jan 1970 00:00:00 GMT",
        description: "A few minutes walking from Plaza Spain. Well connected. Less than 50m to metro and bus stop. Rooms in share and familiar flat in safe area, near the City of Justice. Quiet and clean flat to short stays...There are many restaurants, shopings centers and supermarkets... Optional: Transportation to/from airport.",
        latLng: [
          41.36731735672994,
          2.134957981066059
        ],
        ratePer: "per night",
        microProvider: "air",
        photos: [
          "https://a2.muscache.com/pictures/22319501/large.jpg",
          "https://a1.muscache.com/pictures/14770187/large.jpg",
          "https://a2.muscache.com/pictures/14770604/large.jpg",
          "https://a2.muscache.com/pictures/14770222/large.jpg",
          "https://a1.muscache.com/pictures/14770575/large.jpg",
          "https://a0.muscache.com/pictures/22319512/large.jpg",
          "https://a0.muscache.com/pictures/22319538/large.jpg"
        ],
        link: "http://airbnb.com/rooms/145521",
        responseTime: "N/A",
        address: "Carrer de Badal, Barcelona, Cataluña 08014, Spain",
        roomTypeAlias: "Shared room",
        propertyTypeAlias: "Apartment",
        created: "Thu, 01 Jan 1970 00:00:00 GMT",
        smallInfo: [
          [
            "Accommodates",
            2
          ],
          [
            "Bathrooms",
            1
          ],
          [
            "Bedrooms",
            1
          ],
          [
            "Number of Beds:",
            2
          ]
        ],
        bedCount: 2,
        currencySign: "$",
        bathroomCount: 1,
        bedroomCount: 1,
        _id: "5233838bdb97421b95ab96b6",
        heading: "Quiet and safe rooms with wifi !!!"
      },
      [...]
    ],
    _links: {
      self: {
        href: "api.outpost.travel/placeRentals/",
        title: "placeRentals"
      },
      last: {
        href: "api.outpost.travel/placeRentals/?page=23275",
        title: "last page"
      },
      parent: {
        href: "api.outpost.travel",
        title: "home"
      },
      next: {
        href: "api.outpost.travel/placeRentals/?page=2",
        title: "next page"
      }
    }
  }

GET */[collection]/[id]/*
-------------------------
The `/[collection]/[id]/` GET request returns a single item identical to those found inside `_items` from a regular request with no id. Currently the supported id's are made up of the first three characters of a provider and then a numerical or hexadecimal sequence which is unique to the provider. In the future the `[id]` feature may be replaced by a more robust system such as `/[collection]/[provider]/[id]` along with the current system.

.. code-block:: console

  Request:
  $ curl -i http://api.outpost.travel/placeRentals/air130852/

.. code-block:: javascript

  Response:
  {
    origin: "La Bordeta, Barcelona, Spain",
    roomType: "shared_room",
    logoLV: "img/airbnb_lv.png",
    hostName: "Isa",
    pid: "145521",
    currency: "USD",
    rate: 33,
    captions: [
      "",
      "",
      "",
      "",
      "",
      "",
      ""
    ],
    propertyType: "apartment",
    logoSV: "img/airbnb_sv.png",
    logoDesc: "Discover amazing, unique accommodations in 192 countries. With more than 10 million nights booked worldwide, Airbnb is the world leader in travel rentals.",
    city: "barcelona",
    houseRules: "Respeto hacia las personas que comparten el piso y con el mobiliario en general.",
    fullProvider: "Airbnb",
    mid: "air145521",
    occupancy: 2,
    etag: "e1931f7e487a1612d8e10805e2b67ffa37a31674",
    amenities: [
      "TV",
      "Internet",
      "Wireless Internet",
      "Air Conditioning",
      "Elevator in Building",
      "Washer",
      "Dryer"
    ],
    provider: "airbnb",
    _links: {
      self: {
        href: "api.outpost.travel/placeRentals/5233838bdb97421b95ab96b6/",
        title: "place"
      }
    },
    thumbnail: "https://a2.muscache.com/pictures/22319501/medium.jpg",
    updated: "Thu, 01 Jan 1970 00:00:00 GMT",
    description: "A few minutes walking from Plaza Spain. Well connected. Less than 50m to metro and bus stop. Rooms in share and familiar flat in safe area, near the City of Justice. Quiet and clean flat to short stays...There are many restaurants, shopings centers and supermarkets... Optional: Transportation to/from airport.",
    latLng: [
      41.36731735672994,
      2.134957981066059
    ],
    ratePer: "per night",
    microProvider: "air",
    photos: [
      "https://a2.muscache.com/pictures/22319501/large.jpg",
      "https://a1.muscache.com/pictures/14770187/large.jpg",
      "https://a2.muscache.com/pictures/14770604/large.jpg",
      "https://a2.muscache.com/pictures/14770222/large.jpg",
      "https://a1.muscache.com/pictures/14770575/large.jpg",
      "https://a0.muscache.com/pictures/22319512/large.jpg",
      "https://a0.muscache.com/pictures/22319538/large.jpg"
    ],
    link: "http://airbnb.com/rooms/145521",
    responseTime: "N/A",
    address: "Carrer de Badal, Barcelona, Cataluña 08014, Spain",
    roomTypeAlias: "Shared room",
    propertyTypeAlias: "Apartment",
    created: "Thu, 01 Jan 1970 00:00:00 GMT",
    smallInfo: [
      [
        "Accommodates",
        2
      ],
      [
        "Bathrooms",
        1
      ],
      [
        "Bedrooms",
        1
      ],
      [
        "Number of Beds:",
        2
      ]
    ],
    bedCount: 2,
    currencySign: "$",
    bathroomCount: 1,
    bedroomCount: 1,
    _id: "5233838bdb97421b95ab96b6",
    heading: "Quiet and safe rooms with wifi !!!"
  }

----

GET */count/*
-------------
A `/count/` request will return the sum of all unique items for each provider in the `placeRentals` category. While the request it self is done quite quickly it can take a while to return the data.

.. code-block:: console
  
  Request:
  $ curl -i http://api.outpost.travel/count/

.. code-block:: javascript 

  Response:
  {
    flipkey: 115561,
    waytostay: 3228,
    nflats: 13723,
    geronimo: 1080,
    homeaway: 78925,
    bedycasa: 13276,
    airbnb: 254802,
    holidayvelvet: 4681,
    roomorama: 60557,
    interhome: 36588,
  },
  {
    unique_cities: 53548,
    sum: 582421
  }

GET */count/[provider]/*
------------------------

With the `/[provider]/` option appended the response will now only display a single provider.

.. code-block:: console
  
  Request:
  $ curl -i http://api.outpost.travel/count/flipkey/

.. code-block:: javascript 

  Response:
  {
    flipkey: 115561,
  }

.. _`api.outpost.travel`: http://api.outpost.travel
.. _`Outpost.Travel`: http://outpost.travel/
.. _Github: http://github.com/outposttravel/OutpostPublicAPI
.. _Eve: http://python-eve.org/