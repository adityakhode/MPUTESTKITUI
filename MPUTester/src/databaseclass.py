# Author           : Aditya Khode
# Filename         : databaseclass.py
# Functions        :  __init__ , testTable , check_parameter_range , insertDataFromExcel , resultTable , saveResult , getSingleOrDualNumber , saveDataBase , getSingleOrDualNumber , goToSecondFrame , saveResult , get_average_parameter_value , get_average_parameter_value
# Global Variables : None

import os
import sqlite3
import pandas as pd

class DatabaseClass:

    # Function Name : __init__
    # input         : None 
    # Output        : void
    # Logic         : Establishes the connection between python and sql and creates the table if not exists
    # example       : call Automatically called when object created
    def __init__(self):
        os.makedirs(f"Database/", exist_ok=True)
        self.connection = sqlite3.connect('Database/mydatabase.db')
        self.cursor = self.connection.cursor()
        self.testTable()
        self.resultTable()


    # Function Name : testTable
    # input         : None 
    # Output        : void
    # Logic         : creates the test table in which all the details of parts are present and PRIMARYKEY is partNumber
    # example       : self.testTable()
    def testTable(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS test_table (
                partNumber INTEGER PRIMARY KEY,
                partName VARCHAR(255),
                singleDual INTEGER,
                threading VARCHAR(255),
                length FLOAT,
                Threading_GoNogo_Test VARCHAR(255),
                No_of_Lock_Nuts INTEGER,
                thickness_of_nut FLOAT,
                nut_flat_flat_size FLOAT,
                pin_protrusion_cable FLOAT,
                connector1 VARCHAR(255),
                connector2 VARCHAR(255),
                upperResistance FLOAT,
                lowerResistance FLOAT,
                upperInductance FLOAT,
                lowerInductance FLOAT,
                upperFrequency FLOAT,
                lowerFrequency FLOAT,
                upperVoltage FLOAT,
                lowerVoltage FLOAT
            )
        """
        self.cursor.execute(create_table_sql)
        self.connection.commit()


    # Function Name : check_parameter_range
    # input         : partNumber,paramater and calculated value 
    # Output        : status
    # Logic         : checks if result is in given range
    # example       : object.check_parameter_range()
    # comment       : not implemented fully 
    def check_parameter_range(self, part_no, rpiValue, parameter):
        column_names = {
            'resistance': ('upperResistance', 'lowerResistance'),
            'inductance': ('upperInductance', 'lowerInductance'),
            'frequency': ('upperFrequency', 'lowerFrequency'),
            'voltage': ('upperVoltage', 'lowerVoltage')
        }

        upper_column, lower_column = column_names.get(parameter.lower(), (None, None))
        if not upper_column or not lower_column:
            return f"Invalid parameter: {parameter}"

        self.cursor.execute(f"SELECT {upper_column}, {lower_column} FROM test_table WHERE partNumber=?", (part_no,))
        result = self.cursor.fetchone()
        if result:
            upper_value, lower_value = result
            if lower_value <= rpiValue <= upper_value:
                return f"rpiValue ({rpiValue}) is within the range of {parameter} ({lower_value} - {upper_value})"
            else:
                return f"rpiValue ({rpiValue}) is NOT within the range of {parameter} ({lower_value} - {upper_value})"
        else:
            return f"No record found for part number: {part_no}"


    # Function Name : insertDataFromExcel
    # input         : partNumber,paramater and calculated value 
    # Output        : status
    # Logic         : inserts data to database from exel file
    # example       : object.insertDataFromExcel()
    # comment       : not implemented fully 
    def insertDataFromExcel(self, file_path):
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                self.cursor.execute("INSERT INTO test_table (partNumber, partName, singleDual, threading, length, Threading_GoNogo_Test, No_of_Lock_Nuts, thickness_of_nut, nut_flat_flat_size, pin_protrusion_cable, connector1, connector2, upperResistance, lowerResistance, upperInductance, lowerInductance, upperFrequency, lowerFrequency, upperVoltage, lowerVoltage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                    (row['partNumber'], row['partName'], row['singleDual'], row['Threading'], row['Length'],
                                     row['Threading_GoNogo_Test'], row['No_of_Lock_Nuts'], row['thickness_of_nut'],
                                     row['nut_flat_flat_size'], row['pin_protrusion_cable'], row['connector1'],
                                     row['connector2'], row['upperResistance'], row['lowerResistance'],
                                     row['upperInductance'], row['lowerInductance'], row['upperFrequency'],
                                     row['lowerFrequency'], row['upperVoltage'], row['lowerVoltage']))
            self.connection.commit()
            return "Data inserted successfully."
        except Exception as e:
            return f"Error inserting data: {str(e)}"


    # Function Name : resultTable
    # input         : None 
    # Output        : void
    # Logic         : creates the result table in which all the output details of tested sensor are present PRIMARY KEY is tCNo
    # example       : self.resultTable()
    def resultTable(self):
        self.cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='result_database'
        """)
        if not self.cursor.fetchone():
            create_table_sql = """
            CREATE TABLE result_database (
                tCNo  VARCHAR(255)PRIMARY KEY NOT NULL,
                tCDate DATE,
                supplierCode VARCHAR(255) NOT NULL,
                partyName VARCHAR(255) NOT NULL,
                partName VARCHAR(255) NOT NULL,
                partNumber INTEGER NOT NULL,
                batchNumber VARCHAR(255) NOT NULL,
                challanQTY INTEGER,
                challanNo INTEGER,
                challanDate DATE,
                calResistance1 REAL DEFAULT NULL,
                resistanceStatus1 VARCHAR(255) DEFAULT NULL,
                calInductance1 REAL DEFAULT NULL,
                inductanceStatus1 VARCHAR(255) DEFAULT NULL,
                calFrequency1 REAL DEFAULT NULL,
                frequencyStatus1 VARCHAR(255) DEFAULT NULL,
                calVoltage1 REAL DEFAULT NULL,
                voltageStatus1 VARCHAR(255) DEFAULT NULL,
                calResistance2 REAL DEFAULT NULL,
                resistanceStatus2 VARCHAR(255) DEFAULT NULL,
                calInductance2 REAL DEFAULT NULL,
                inductanceStatus2 VARCHAR(255) DEFAULT NULL,
                calFrequency2 REAL DEFAULT NULL,
                frequencyStatus2 VARCHAR(255) DEFAULT NULL,
                calVoltage2 REAL DEFAULT NULL,
                voltageStatus2 VARCHAR(255) DEFAULT NULL
            );
            """
            self.cursor.execute(create_table_sql)
            self.connection.commit()

    # Function Name : saveResult
    # input         : (tCNo, tCDate, supplierCode, partyName, partName, partNumber, batchNumber,
    #                 challanQTY, challanNo, challanDate, calResistance, resistanceStatus,
    #                 calInductance, inductanceStatus, calFrequency, frequencyStatus,
    #                 calVoltage, voltageStatus)
    # Output        : void
    # Logic         : Saves the result to database
    # example       : object.saveResult()
    def saveResult(self, tCNo, tCDate, supplierCode, partyName, partName, partNumber, batchNumber,
                   challanQTY, challanNo, challanDate, calResistance, resistanceStatus,
                   calInductance, inductanceStatus, calFrequency, frequencyStatus,
                   calVoltage, voltageStatus,calResistance2, resistanceStatus2,
                   calInductance2, inductanceStatus2, calFrequency2, frequencyStatus2,
                   calVoltage2, voltageStatus2):
        insert_query = """
        INSERT INTO result_database (tCNo, tCDate, supplierCode, partyName, partName, partNumber,
                                     batchNumber, challanQTY, challanNo, challanDate, calResistance1,
                                     resistanceStatus1, calInductance1, inductanceStatus1, calFrequency1,
                                     frequencyStatus1, calVoltage1, voltageStatus1,calResistance2, resistanceStatus2,
                   calInductance2, inductanceStatus2, calFrequency2, frequencyStatus2,
                   calVoltage2, voltageStatus2)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = (tCNo, tCDate, supplierCode, partyName, partName, partNumber, batchNumber,
                  challanQTY, challanNo, challanDate, calResistance, resistanceStatus,
                  calInductance, inductanceStatus, calFrequency, frequencyStatus,
                  calVoltage, voltageStatus,calResistance2, resistanceStatus2,
                   calInductance2, inductanceStatus2, calFrequency2, frequencyStatus2,
                   calVoltage2, voltageStatus2)
        try:
            self.cursor.execute(insert_query, values)
            self.connection.commit()
            return "Result saved successfully."
        except Exception as e:
            return f"Error saving result: {str(e)}"


    # Function Name : getSingleOrDualNumber
    # input         : partNumber 
    # Output        : 1 or 2
    # Logic         : Returns the MPU sensor has single or Dual output
    # example       : object.getSingleOrDualNumber()
    def getSingleOrDualNumber(self, no):
        try:
            self.cursor.execute("SELECT singleDual FROM test_table WHERE partNumber=?", (no,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return "No record found for part number: {}".format(no)
        except Exception as e:
            return "Error retrieving single/dual number: {}".format(str(e))


    # Function Name : get_average_parameter_value
    # input         : partNumber and paramater (Resistance , inductance , voltage , frequency)
    # Output        : average number
    # Logic         : Returns the average of maximum and minimum of that paramater
    # example       : object.get_average_parameter_value()
    def get_average_parameter_value(self, part_number, parameter):
        column_names = {
            'resistance': ('upperResistance', 'lowerResistance'),
            'inductance': ('upperInductance', 'lowerInductance'),
            'frequency': ('upperFrequency', 'lowerFrequency'),
            'voltage': ('upperVoltage', 'lowerVoltage')
        }

        upper_column, lower_column = column_names.get(parameter.lower(), (None, None))
        if not upper_column or not lower_column:
            return f"Invalid parameter: {parameter}"

        self.cursor.execute(f"SELECT {upper_column}, {lower_column} FROM test_table WHERE partNumber=?", (part_number,))
        result = self.cursor.fetchone()
        if result:
            upper_value, lower_value = result
            # Calculate average of maximum and minimum values
            average_value = (upper_value + lower_value) / 2
            return average_value
        else:
            return f"No record found for part number: {part_number}"
        

    # Function Name : get_result_by_tcno
    # input         : testCertificate Number
    # Output        : list of result given by the hardware
    # Logic         : used sql to get and save it in variable and convert it into array list
    # example       : object.get_result_by_tcno()    
    def get_result_by_tcno(self, tc_no):
        desired_columns = (
            "calResistance1", "resistanceStatus1", "calInductance1", "inductanceStatus1",
            "calFrequency1", "frequencyStatus1", "calVoltage1", "voltageStatus1",
            "calResistance2", "resistanceStatus2", "calInductance2", "inductanceStatus2",
            "calFrequency2", "frequencyStatus2", "calVoltage2", "voltageStatus2"
        )

        query = f"SELECT {', '.join(desired_columns)} FROM result_database WHERE tCNo = ?"
        self.cursor.execute(query, (tc_no,))
        result = self.cursor.fetchone()

        if result:
            return list(result)  # Convert the fetched row to a list
        else:
            return None  # Indicate no record found

