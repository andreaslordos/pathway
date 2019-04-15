import requests

def getRoadRisk(lat,long):
    def getStreetName(lat,long):
        api_key = "AIzaSyDBleOeXH-sdJUokiyjGioMnzAk44c-qpM"
        full_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+','.join((str(lat),str(long)))+"&result_type=street_address&key=AIzaSyDBleOeXH-sdJUokiyjGioMnzAk44c-qpM"
        html = requests.get(full_url)
        clean = html.content
        clean_str = str(clean)
        clean_list = clean_str.split("\\n")
        e = "".join(clean_list)
        f = e.split(" ")
        g = "".join(f)
        data = g[2:-1]
        street = eval(str(data))
        return street
    return getStreetName(lat,long)
