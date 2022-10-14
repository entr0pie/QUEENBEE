import json

class ShowInfo:            
    def show_info(self, content):
        for e in content:
            content[e] = self.__clean_text__(content[e])

        content["description"] = self.__add_paragraph__(content["description"])
        content["input"] = self.__add_paragraph__(content["input"])
        content["output"] = self.__add_paragraph__(content["output"])

        text =  f'- LINK: {content["link"]}'
        text += f'- TITLE: {content["title"]}'
        text += f'- AUTHOR: {content["author"]}'
        text += f'- TIMELIMIT: {content["timelimit"]}\n'
        text += f'- DESCRIPTION:\n{content["description"]}'
        text += f'- INPUT: {content["input"]}'
        text += f'- OUTPUT: {content["output"]}'

        text += '----------------------------\n'
        text += f'INPUT EXAMPLE:\n'
        text += '----------------------------\n'
        text += f'{content["input-example"]}\n'
        text += '----------------------------\n'
        text += f'OUTPUT EXAMPLE:\n'
        text += '----------------------------\n'
        text += f'{content["output-example"]}\n'
        text += '----------------------------'
        print(text)

    def __clean_text__(self, text:str):
        text = text.split('\n')        
        cleaned = []
        for l in range(len(text)):
            if text[l] != "":
                cleaned.append(text[l].replace('\n', '').strip() + '\n')

        cleaned_txt = ""
        for t in cleaned:
            cleaned_txt += t

        return cleaned_txt


    def __add_paragraph__(self, text:str):
        text = text.replace('.', f'.\n')
        return text

