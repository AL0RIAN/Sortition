from docx import Document #Main python DOCX class
from docx.shared import Pt, Cm #Points, Centimeters
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT #Paragraph alignment
from docx.oxml.shared import OxmlElement, qn #Magic
from os import path as os_path #Working with external files

'''
Sample data.
Contains test data, that can be exported in DOCX file.

:param start-date - The day tournament is starting
:param end-date - The day tournament is ending
:param pairs - A pair of two participants
    :param is-circle-trinity - If there's three participants in circle trinity, then True, else False
    :param age-category - Info about pair participants age category
    :param weight-category - Info about pair participants weight category
    :param red/blue - Contestant
        :param last-name - Last name of contestant
        :param first-name - First name of contestant
        :param club - The club contestant is in


For sample purpose only.
'''
sample_data = {
    "start-date": "21.04.2022",
    "end-date": "23.03.2022",
    "pairs": [
        {
            "is-circle-trinity": True,
            "age-category": "8-9",
            "weight-category": "44",
            "red": {
                "last-name": "Виенко",
                "first-name": "Богдан",
                "club": "Саньда"
            },

            "blue": {
                "last-name": "Рублев",
                "first-name": "Дмитрий",
                "club": "Патриот"
            }
        },

        {
            "is-circle-trinity": False,
            "age-category": "8-9",
            "weight-category": "44",
            "red": {
                "last-name": "Виенко",
                "first-name": "Богдан",
                "club": "Саньда"
            },

            "blue": {
                "last-name": "Рублев",
                "first-name": "Дмитрий",
                "club": "Патриот"
            }
        }
    ]
}

class Participant:
    """
    Class that represents info about particular contestant

    :param last_name: Last name of contestant
    :param first_name: First name of contestant
    :param club: The club contestant is in
    """

    def __init__(self, last_name: str, first_name: str, club: str):
        '''

        :param last_name: Last name of contestant
        :param first_name: First name of contestant
        :param club: The club contestant is in
        '''
        self.last_name = last_name
        self.first_name = first_name
        self.club = club


class Pair:
    """
    Class that represents info about particular pair of contestants

    :param is-circle-trinity: If there's three participants in circle trinity, then True, else False
    :param age-category: Info about pair participants age category
    :param weight-category: Info about pair participants weight category
    :param red/blue: Contestant
    """

    def __init__(self, is_circle_trinity: bool, age_category: str, weight_category: str,
                 red: Participant, blue: Participant):
        '''

        :param is_circle_trinity: If there's three participants in circle trinity, then True, else False
        :param age_category: Info about pair participants age category
        :param weight_category: Info about pair participants weight category
        :param red: Contestant
        :param blue: Contestant
        '''
        self.is_circle_trinity = is_circle_trinity
        self.age_category = age_category
        self.weight_category = weight_category
        self.red = red
        self.blue = blue


class ExportDOCX:
    """Main DOCX export class, that converts parsed info into DOCX file."""

    __DEFAULT_DATA = {
        "start-date": "",
        "end-date": "",
        "pairs": []
    }

    def __init__(self, start_date: str = "{{start-date}}", end_date: str = "{{end-date}}",
                 data: dict = __DEFAULT_DATA):
        '''

        :param start_date: The day tournament is starting
        :param end_date: The day tournament is ending
        :param data: Contains data, that will be exported in DOCX file.
        '''
        if __name__ == "__main__": #If this file is runned, then base.docx is in the same folder as this file
            self.__document = Document(os_path.abspath("base.docx"))
        else: #Else base.docx is in the same folder as this file, but because this file is imported, you have to do this
            self.__document = Document(os_path.abspath("export\\base.docx"))
        self.start_date = start_date
        self.end_date = end_date
        self.__table = self.__document.tables[0] #Only one table is needed
        self.__data = data

    def __print_dates(self) -> None:
        '''
        Prints dates in the start of exporting file

        :return: None
        '''
        for paragraph in self.__document.paragraphs:
            for run in paragraph.runs:
                if run.text == "{{start-date}}":
                    run.text = self.start_date

                if run.text == "{{end-date}}":
                    run.text = self.end_date

    def __print_table(self) -> None:
        '''
        Prints containing in __data info into file table

        :return: None
        '''
        count = 1 #Left table column

        for pair in self.__data["pairs"]:
            row = self.__table.add_row()
            row.height = Cm(0.6)
            row_cells = row.cells

            row_cells[0].text = str(count)
            row_cells[0].paragraphs[0].runs[0].font.name = "Century Gothic"
            row_cells[0].paragraphs[0].runs[0].font.size = Pt(10)
            row_cells[0].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

            row_cells[1].text = f"{pair['age-category']} лет\n{pair['weight-category']} кг"
            row_cells[1].paragraphs[0].runs[0].font.bold = True
            row_cells[1].paragraphs[0].runs[0].font.size = Pt(9)
            row_cells[1].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

            '''RED'''
            row_cells[2].text = f"{pair['red']['last-name']} {pair['red']['first-name']}"
            row_cells[2].paragraphs[0].runs[0].font.size = Pt(10)
            row_cells[2].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

            row_cells[3].text = pair['red']['club']
            row_cells[3].paragraphs[0].runs[0].font.size = Pt(9)
            row_cells[3].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

            row_cells[4].text = "Кругов." if pair['is-circle-trinity'] else ""
            row_cells[4].paragraphs[0].runs[0].font.bold = True
            row_cells[4].paragraphs[0].runs[0].font.size = Pt(8)
            row_cells[4].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

            '''BLUE'''
            row_cells[5].text = f"{pair['blue']['last-name']} {pair['blue']['first-name']}"
            row_cells[5].paragraphs[0].runs[0].font.size = Pt(10)
            row_cells[5].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            row_cells[6].text = pair['blue']['club']
            row_cells[6].paragraphs[0].runs[0].font.size = Pt(9)
            row_cells[6].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

            for i in range(7):
                row_cells[i].paragraphs[0].paragraph_format.space_after = Cm(0)

                '''
                Кирилл или Ярик, если вы это смотрите, я сам не знаю как работает это колесо сансары
                '''
                tc = row_cells[i]._tc
                tcPr = tc.get_or_add_tcPr()
                tcValign = OxmlElement('w:vAlign')
                tcValign.set(qn('w:val'), "center")
                tcPr.append(tcValign)

            count += 1

    def add_pair(self, pair: Pair) -> None:
        '''
        Adds one pair to __data.

        :param pair: instance of Pair class.
        :return: None
        '''

        new_pair = {
            "is-circle-trinity": False,
            "age-category": "",
            "weight-category": "",
            "red": {
                "last-name": "",
                "first-name": "",
                "club": ""
            },

            "blue": {
                "last-name": "Рублев",
                "first-name": "Дмитрий",
                "club": "Патриот"
            }
        }

        new_pair["is-circle-trinity"] = pair.is_circle_trinity
        new_pair["age-category"] = pair.age_category
        new_pair["weight-category"] = pair.weight_category

        new_pair["red"]["last-name"] = pair.red.last_name
        new_pair["red"]["first-name"] = pair.red.first_name
        new_pair["red"]["club"] = pair.red.club

        new_pair["blue"]["last-name"] = pair.blue.last_name
        new_pair["blue"]["first-name"] = pair.blue.first_name
        new_pair["blue"]["club"] = pair.blue.club

        self.__data["pairs"].append(new_pair)


    def export(self, path="") -> None:
        '''
        Congratulations! You're exporting a file. Leave path empty to export in root folder

        :param path: Path where to save export file
        :return: None
        '''
        self.__print_dates()
        self.__print_table()
        if path != "":
            self.__document.save(os_path.abspath(f"{path}/Состав пар турнир {self.start_date} - {self.end_date}.docx"))
        else:
            self.__document.save(f"Состав пар турнир {self.start_date} - {self.end_date}.docx")
