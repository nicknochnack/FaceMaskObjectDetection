{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. Getting Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import opencv\n",
    "import cv2 \n",
    "\n",
    "# Import uuid\n",
    "import uuid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  Image capture\n",
    "cap = cv2.VideoCapture(2)\n",
    "width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))\n",
    "height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "while True: \n",
    "    ret, frame = cap.read()\n",
    "    imgname = './Images/No Mask/{}.jpg'.format(str(uuid.uuid1()))\n",
    "    cv2.imwrite(imgname, frame)\n",
    "    cv2.imshow('frame', frame)\n",
    "    \n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cap.release()\n",
    "cap.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.1 Training Model - Watson Studio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Done"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2. Scoring"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "from ibm_watson import VisualRecognitionV4\n",
    "from ibm_watson.visual_recognition_v4 import FileWithMetadata, AnalyzeEnums\n",
    "from ibm_cloud_sdk_core.authenticators import IAMAuthenticator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "apikey = 'YOUR API KEY HERE'\n",
    "url = 'YOUR URL HERE'\n",
    "collection = 'YOUR COLLECTION HERE'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "authenticator = IAMAuthenticator(apikey)\n",
    "service = VisualRecognitionV4('2018-03-19', authenticator=authenticator)\n",
    "service.set_service_url(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "path = 'PATH TO YOUR IMAGE'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(path, 'rb') as mask_img:\n",
    "    analyze_images = service.analyze(collection_ids=[collection], \n",
    "                                     features=[AnalyzeEnums.Features.OBJECTS.value], \n",
    "                                    images_file=[FileWithMetadata(mask_img)]).get_result()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "analyze_images"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3. Visualise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "obj = analyze_images['images'][0]['objects']['collections'][0]['objects'][0]['object']\n",
    "coords = analyze_images['images'][0]['objects']['collections'][0]['objects'][0]['location']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "coords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = cv2.imread(path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "font = cv2.FONT_HERSHEY_SIMPLEX\n",
    "img = cv2.putText(img, text=obj, org=(coords['left']+coords['width'], coords['top']+coords['height']), fontFace=font, fontScale=2, color=(0,255,0), thickness=5, lineType=cv2.LINE_AA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.imshow(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "obj"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
