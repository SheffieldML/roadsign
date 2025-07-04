from distutils.core import setup
setup(
  name = 'roadsign',
  packages = ['roadsign'],
  version = '0.0.1',
  description = 'Open Day roadsign activity',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/SheffieldML/roadsign.git',
  download_url = 'https://github.com/SheffieldML/roadsign.git',
  keywords = ['open day','adversarial examples','road signs'],
  classifiers = [],
  install_requires=['yolov5 @ git+https://github.com/SheffieldML/yolov5-pip.git','opencv-python==4.7.0.68'],
  scripts=['bin/openday']
)

