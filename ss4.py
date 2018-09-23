


def save_fullpage_screenshot(url, output_path, tmp_prefix='selenium_screenshot', tmp_suffix='.png'):
    """
    Creates a full page screenshot using a selenium driver by scrolling and taking multiple screenshots,
    and stitching them into a single image.
    """
 
    from selenium import webdriver
    import math
    import tempfile
    import os
    from keras.preprocessing import image

    # get the page
    driver = webdriver.Firefox()
    driver.get(url)
 
    # get dimensions
    window_height = driver.execute_script('return window.innerHeight')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    num = int( math.ceil( float(scroll_height) / float(window_height) ) )
 
    # get temp files
    tempfiles = []
    for i in range( num ):
        fd,path = tempfile.mkstemp(prefix='{0}-{1:02}-'.format(tmp_prefix, i+1), suffix=tmp_suffix)
        os.close(fd)
        tempfiles.append(path)
        pass
 
    try:
        # take screenshots
        for i,path in enumerate(tempfiles):
            if i > 0:
                driver.execute_script( 'window.scrollBy(%d,%d)' % (0, window_height) )
             
            driver.save_screenshot(path)
            pass
         
        # stitch images together
        stiched = None
        for i,path in enumerate(tempfiles):
            img = Image.open(path)
             
            w, h = img.size
            y = i * window_height
             
            if i == ( len(tempfiles) - 1 ):
                img = img.crop((0, h-(scroll_height % h), w, h))
                w, h = img.size
                pass
             
            if stiched is None:
                stiched = Image.new('RGB', (w, scroll_height))
             
            stiched.paste(img, (
                0, # x0
                y, # y0
                w, # x1
                y + h # y1
            ))
            pass
        stiched.save(output_path)
    finally:
        # cleanup
        for path in tempfiles:
            if os.path.isfile(path):
                os.remove(path)
        pass
 
    return output_path

save_fullpage_screenshot(url='http://www.iherb.com', output_path='output\myss4.png', tmp_prefix='selenium_screenshot', tmp_suffix='.png')
