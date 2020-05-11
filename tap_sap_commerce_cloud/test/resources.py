product_search_list = {
    'type': 'productCategorySearchPageWsDTO',
    'breadcrumbs': [],
    'currentQuery': {},
    'facets': [],
    'freeTextSearch': '',
    'pagination': {
        'currentPage': 0,
        'pageSize': 100,
        'sort': 'relevance',
        'totalPages': 1,
        'totalResults': 2
    },
    'products': [
        {
            'availableForPickup': True,
            'code': '123456',
            'name': 'Product',
            'price': {
                'currencyIso': 'CAD',
                'value': 100.00
            },
            'stock': {
                'stockLevel': 4
            },
            'url': ''
        },
        {
            'availableForPickup': True,
            'code': '234567',
            'name': 'Product',
            'price': {
                'currencyIso': 'CAD',
                'value': 29.99
            },
            'stock': {
                'stockLevel': 12
            },
            'url': ''
        }
    ]
}

product_details = {
    '123456': {
        'availableForPickup': True,
        'averageRating': 0,
        'code': '123456',
        'configurable': False,
        'configuratorType': '',
        'description': 'Product description',
        'images': [
            {
                'format': 'thumbnail',
                'imageType': 'PRIMARY',
                'url': '/medias/thumbnail'
            },
            {
                'format': 'product',
                'imageType': 'PRIMARY',
                'url': '/medias/product'
            }
        ],
        'manufacturer': 'Manufacturer',
        'multidimensional': False,
        'name': 'Product',
        'price': {
            'currencyIso': 'CAD',
            'formattedValue': '$100.00',
            'priceType': 'BUY',
            'value': 100.00
        },
        'priceRange': {},
        'stock': {
            'stockLevel': 4,
            'stockLevelStatus': 'lowStock'
        },
        'summary': 'Product summary',
        'url': '',
        'volumePricesFlag': False
    },
    '234567': {
        'availableForPickup': True,
        'averageRating': 0,
        'code': '234567',
        'configurable': False,
        'configuratorType': '',
        'description': 'Product description',
        'images': [
            {
                'format': 'thumbnail',
                'imageType': 'PRIMARY',
                'url': '/medias/thumbnail'
            },
            {
                'format': 'product',
                'imageType': 'PRIMARY',
                'url': '/medias/product'
            }
        ],
        'manufacturer': 'Manufacturer',
        'multidimensional': False,
        'name': 'Product',
        'price': {
            'currencyIso': 'CAD',
            'formattedValue': '$29.99',
            'priceType': 'BUY',
            'value': 29.99
        },
        'priceRange': {},
        'stock': {
            'stockLevel': 12,
            'stockLevelStatus': 'lowStock'
        },
        'summary': 'Product summary',
        'url': '',
        'volumePricesFlag': False
    },
}