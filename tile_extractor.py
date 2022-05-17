def extract_tiles(wsi_files, geo_files, path_to_save, tile_size = 256):
    # Написать описание функции
    
    import openslide
    import geojson
    import os, platform
    
    files_count = len(wsi_files) # number of slides to process
    zip_dir = zip(wsi_files, geo_files)
    
    def extract_tiles (slide_path, geojson_path, path_to_save):
        # Написать описание функци        

        # open slide from directory
        slide = openslide.OpenSlide(slide_path)
        # open geojson
        with open(geojson_path) as file:
            geo_data = geojson.load(file)
        
        # extract tiles 
        for feature in geo_data:

            class_name = feature['properties']['classification']['name'] # Class of the tile image
            try:
                x,y = feature['geometry']['coordinates'][0][0] # coordinates of the left corner of the tile to extract
            except:
                x,y = feature['geometry']['coordinates'][0][0][0]

            tile = slide.read_region(location = (int(x),int(y)),level = 0,size = (tile_size,tile_size)) # create tile from slide, using x,y coordinates

            patient_id = geojson_path.split('\\')[-1].split('.')[0] # get unique patien_id to use it in tile name
            
            tile = tile.convert('RGB')# if you want jpeg format!!!
            
            ex_path = path_to_save + '\\' + class_name + '\\' + patient_id +'_' + 'x=' + str(x) + '_' + 'y=' + str(y)+'.jpeg'
            tile.save(ex_path)
    
    
    print('Slides to process : ' + str(files_count))
    counter = 0
    for directory in zip_dir:
        slide_path = directory[0]
        geojson_path = directory[1]
        print('Now processing: '+ slide_path)
        extract_tiles(slide_path, geojson_path, path_to_save )
        print()
        counter+=1
        print('Remain slides : ' + str(files_count - counter))
    print('Complete!')

def get_files_from_dir (dir_path):
    # ОПИСАНИЕ!!!!
    from os import listdir
    files = list()
    for file in listdir(dir_path):
        files.append(dir_path + '\\' + file )
    return files

