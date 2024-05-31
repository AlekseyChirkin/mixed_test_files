class CommentFromWebSite():
    """_summary_

    """

    def __init__(self, date, text, likes):
        self.__date = date
        self.__text = text
        self.__likes = likes

    def get_date(self):
        """
        Function returns date of comment

        Returns:
            str: date of writing comment
        """
        info = self.__date
        return info

    def get_likes(self) -> int:
        """
        Function returns likes count

        Returns:
            int: likes count
        """
        info = self.__likes
        return info

    def get_text(self) -> str:
        """
        Function returns text from "text" attribute

        Returns:
            str: text of comment
        """
        info = self.__text
        return info

    def set_date(self, date):
        """
        Function sets new date to "date" attribute
        """
        self.__date = date

    def set_likes(self, likes):
        """
        Function sets new count of likes
        """
        self.__likes = likes

    def set_text(self, text):
        """
        Function sets new date to "text" attribute
        """
        self.__text = text

    def like_button_pushed(self):
        """
        Increase likes attribute +1
        """
        self.__likes += 1

    def __str__(self) -> str:
        return f"-----------------------\nДата: {self.get_date()}\nКомментарий: \"{self.get_text()}\"\nКоличество лайков: ♡ {self.get_likes()}\n-----------------------"


new_comment = CommentFromWebSite("10.10.10", "Первыйнах", 100500)
print(type(new_comment))

print(new_comment.get_date(), type(new_comment.get_date()))
print(new_comment.get_likes())
new_comment.like_button_pushed()
print(new_comment.get_likes())
new_comment.like_button_pushed()
print(new_comment.get_likes())
new_comment.like_button_pushed()
print(new_comment.get_text())
print(new_comment)
