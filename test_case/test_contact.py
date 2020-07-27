from appiumwework.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start_app().main()
    def test_contact(self):
        toast = self.main.goto_contact().add_member().manual_input().name_input().gender_select()\
            .phone_numer().click_save().back_button().find_del_mem('test8')\
            .person_info().editor_memmber().del_mem()
        #assert "成功" in toast.get_toast()




