def extract_tiles(wsi_files, geo_files, path_to_save, tile_size = 256):
    """ Extract images (256x256)  from slides to directory in jpeg format
    ----------------------------------------------------------------
    Parameters:
    wsi_files (list) - list of paths to WSI slides
    geo_files (list) - list of paths to GeoJson files
    path_to_save (str) - path to the folder where the images will be saved. IMPORTANT : it should contain folders named after classes (main folder ---> class1 -->
                                                                                                                                                        class2 -->
                                                                                                                                                        class3 -->
     tile_size (int) - size in pixels of the output image"""
    
    import openslide  # Can i import libraries in function ?
    import geojson
    import os, platform
    
    files_count = len(wsi_files) # number of slides to process
    zip_dir = zip(wsi_files, geo_files)
    
    def extract_images_from_slide (slide_path, geojson_path, path_to_save):
        """ Extract images from one WSI, using coordinates from GeoJson (Pretty Json) file
        -----------------------------------------------------------------------------
        Parameters:
        slide_path (str) - path to WSI slide
        geojson_path (str) - path to json file
        path_to_save (str) - path to the folder where the images will be saved. IMPORTANT : it should contain folders named after classes (main folder ---> class1 -->
                                                                                                                                                            class2 -->
                                                                                                                                                            class3 -->
        """      

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
        extract_images_from_slide(slide_path, geojson_path, path_to_save )
        print()
        counter+=1
        print('Remain slides : ' + str(files_count - counter))
    print('Complete!')

def get_files_from_dir (dir_path):
    """ Return list of files (filepath) in directory 
    ------------------------------------------------
    Parameters : 
    dir_path(str) - path to directory in string format
    
    Output : files - list of pathes"""
    from os import listdir
    files = list()
    for file in listdir(dir_path):
        files.append(dir_path + '\\' + file )
    return files

