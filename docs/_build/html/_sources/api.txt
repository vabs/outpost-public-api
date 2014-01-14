GET */*
-------
Currently a GET request of the root page will redirect the user to this documentation. It is planned in the future for the index page to contain an index of all the links one step down from index (/count,/places,/experiences,...)

GET */[collection]/*
--------------------
This GET request requires on of three possible collections. Possible collections are `places`, `rideshares` and `experiences`. The response will contain five objects, the current page number, the total number of pages, the limit or results per page, the total number of results and an `items` array. The `items` array contains 20 items which are either places for the `places` collection, rides for `rideshares` and experiences for `experiences`. The schema is identical for all items in a collection and are quite similar between collections.

**Options:**

  **Pagination:**

  `page`:
    `page` is to be used for pagenation as expected. The correct syntax for `page` is `?page=pageNumber`. If the page requested is greater than those avaliable the response will include an empty `items` array.
  
  `limit`:
    `limit` is to be used with or without pagenation to limit the number or results shown in the `items` array. The correct syntax for `max_results` is `?max_results=numResults`. The maximum number of results is currently set at 50 results per page and the minimum is 1. If the number is greater or lower than said limits, the page will return 20 results as the default.

  **Location based queries:**

  `dest`:
    `city` can be used to query results that only are for a certain city. `latLng` will provider a query of the area which may include other municipalites. The proper syntax is `?dest=city`. You can then use `sort` (explained later), to sort by `latLng` or any other key.

  `latLng`:
    `latLng` is similar to `dest` but query a specific latitude and longitude. This will then return all the listings within a radius of a 1-15 kilometers. In the future there will be a option to set the radius via `?radius=1000` for 1 kilometer. The proper syntax for `latLng` is `?latLng=latitude,longitude`.


  **Sorting:**

  `sort`:
    `sort` can be used to sort specific items in ascending order. The syntax is `?sort=itemKey`. Item keys are to be used such as price, city or provider.
  `sortMethod`:
    `sortMethod` is to be used with `sort` to display the results in an ascending or descending order based on the value given. The syntax is `?sortMethod=method` where the method is either `1` for ascending or `-1` for descending.


  **Filtering:**

  `priceMin` and `priceMax`:
    `priceMin` and `priceMax` can be using in conjunction or seperatly to filter out items who's price is outside of the range given. The lower limit is 0 and there is now upper limit. The syntax is `?priceMin=0&priceMax=1200`.

  `provider`:
    `provider` can be used to filter out providers. The syntax is `?provider=nflats,airbnb,roomorama` to only find listings with those providers.

  `guestMin` and `guestMax`:
    `guestMin` and `guestMax` are to be used the same way as `priceMin` and `priceMax`.

  `bedMin`:
    `bedMin` is to filter by number of beds. The sytax is `?bedMin=1`.

  `bedroomMin`:
    `bedroomMin` is the same as `bedMin` but is for bedrooms.
  
  `washroomMin`:
    `washroomMin` is the same as `bedMin` and `bedroomMin` but is for washrooms.

All the previous options can be used for both the collections and collection/city GET requests.

.. code-block:: console

  Request:
  $ curl -i http://api.outpost.travel/places/

.. code-block:: javascript

  Response:
  {
    page: 1,
    totalPages: 39501,
    resultsPerPage: 20,
    totalResults: 790017,
    items: [
    {
      pid: "bca19413",
      bedCount: -1,
      unavailable: [ ],
      occupancy: 2,
      priority: 0.22705,
      amenities: [ ],
      location: {
        type: "Point",
        coordinates: [
          -1.1737357,
          44.6560411
        ]
      },
      provider: "bedycasa",
      type: {
        roomType: "entire_place",
        propType: "apartment"
      },
      latLng: [
        44.6560411,
        -1.1737357
      ],
      description: "Lodging, in Arcachon at Marie-Pierre's, from 45 EUR per night per one person ! Discover Arcachon, and enjoy the benefits of homestay: practical advice, friendliness and low prices. This is a/an Â« Lodging Â» with a capacity of 2 person(s).",
      price: 62,
      photos: [
        {
          url: "http://www.bedycasa.com/media/cache/room_gallery_bedycasa/uploads/r/19413/511b6b61aecdf.jpg",
          caption: ""
        },
        {
          url: "http://www.bedycasa.com/media/cache/room_gallery_bedycasa/uploads/r/19413/511b6c56a1b66.jpg",
          caption: ""
        },
        {
          url: "http://www.bedycasa.com/media/cache/room_gallery_bedycasa/uploads/r/19413/511bb0bc792c5.jpg",
          caption: ""
        }
      ],
      link: "http://www.bedycasa.com/apartment-flat/arcachon-19413?utm_source=Outpost&utm_medium=XML&utm_campaign=bca19413",
      nid: "19413",
      address: {
        city: "Arcachon",
        country: "France",
        zipcode: "33120",
        suburb: "Ville d'Hiver",
        state: "Aquitaine",
        streetName: "AllÃ©e du Docteur Fernand Lalesque"
      },
      options: {
        preferredPricePer: 1,
        instantBookable: false,
        checkIn: "",
        minimumStayNight: 1,
        houseRules: "",
        responseTime: "24h",
        cancellationRule: "",
        checkOut: "",
        size: "20 mÂ²"
      },
      bathroomCount: -1,
      bedroomCount: -1,
      heading: "Apartment/Flat in Arcachon, at Marie-Pierre's place",
      typeAlias: {
        roomType: "Lodging",
        propType: "Apartment/Flat"
      }
    }]
  }

GET */[collection]/[city]/*
---------------------------
See above.

GET */[collection]/[city][id]/*
-------------------------------
The `/[collection]/[city]/[id]/` GET request returns a single item identical to those found inside `items` from a regular request with no id. Currently the supported id's are made up of the first three characters of a provider and then a numerical or hexadecimal sequence which is unique to the provider. In the future the `[id]` feature may be replaced by a more robust system such as `/[collection]/[provider]/[id]` along with the current system. `[city]` is not technicaly needed but it will speed up the requests.

.. code-block:: console

  Request:
  $ curl -i http://api.outpost.travel/places/spain/air130852/

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
A `/count/` request will return the sum of all unique items for each provider in the `places` and `experiences` categories. While the request it self is done quite quickly it can take a while to return the data.

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
    total: 582421
  }

.. _`api.outpost.travel`: http://api.outpost.travel
.. _`Outpost.Travel`: http://outpost.travel/
.. _Github: http://github.com/outposttravel/OutpostPublicAPI
.. _Eve: http://python-eve.org/