import os
import cv2
import qrcode
from PIL import Image


class pdfAndQr:

    # Function Name : makeQr
    # input         : list to paramater to be displayed on qr see from database function "get_result_by_tcno"  and testCertificate Number
    # Output        : void
    # Logic         : make custom qr code using library
    # example       : makeQr(list , tc number)
    def makeQr(result,tc_no):

        #makes testdata/testCertificate number directory
        os.makedirs(f"testData/{tc_no}", exist_ok=True)

        #qrcode text string
        image_url = f"""Company Name : Twintech Control System Pvt Ltd
        Resistance of 1st Coil {result[0]} and status is {result[1]}
        Resistance of 2nd Coil {result[2]} and status is {result[3]}
        Inductance of 1st Coil {result[4]} and status is {result[5]}
        Inductance of 2nd Coil {result[6]} and status is {result[7]}
        Voltage    of 1st Coil {result[8]} and status is {result[9]}
        Voltage    of 2nd Coil {result[10]} and status is {result[11]}
        frequency  of 1st Coil {result[12]} and status is {result[13]}
        frequency  of 2nd Coil {result[14]} and status is {result[15]}
        """

        # Create a QR code with desired settings
        qr = qrcode.QRCode(
            version=10,  # Adjust version for data size
            box_size=5,  # Adjust box size for visual appeal
            border=4  
        )
        qr.add_data(image_url)
        qr.make(fit=True)

        # Create an image with default colors
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(f"testData/{tc_no}/{tc_no}.png")


    # Function Name : makePdf
    # input         : list to paramater to be displayed on qr see from database function "get_result_by_tcno"  and testCertificate Number
    # Output        : void
    # Logic         : takes image process it save it read it convert it into pdf and delete the processed image 
    # example       : makePdf(tc Number)
    # comment       : not implemented fully
    def makePdf(tc_no):

        #makes testdata/testCertificate number directory
        os.makedirs(f"testData/{tc_no}/", exist_ok=True)

        #dummy certificate path
        image_path = "supportingDocx/certificate.jpg" 
        try:
            # Read the image using cv2.imread()
            image = cv2.imread(image_path)

            # Check if image reading was successful
            if image is None:
                print(f"Error: Could not read image from {image_path}")
                return  # Exit the function if image reading fails

            # Add the text to the image using cv2.putText() (unchanged)
            text = tc_no
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 0)  # Black text
            thickness = 1
            text_x = 245
            text_y = 475
            cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)
            
            cv2.imwrite(f"{tc_no}.png", image)

            image = Image.open(f"{tc_no}.png")
            pdf_path = f'testData/{tc_no}/{tc_no}.pdf'
            
            image.save(pdf_path, "PDF")
            
            if os.path.exists(f"{tc_no}.png"):
                os.remove(f"{tc_no}.png")


        except Exception as e:
            print(f"An error occurred: {e}")
