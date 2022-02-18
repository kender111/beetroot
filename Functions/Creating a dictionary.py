def make_country(country, capital, **country_info):
    country_dict = {}
    country_dict['country'] = country
    country_dict['capital'] = capital
    for key, value in country_info.items():
      country_dict[key] = value
    return country_dict

if __name__ == '__main__':
    my_country = make_country('Ukraine', 'Kyiv')
    print(my_country)
