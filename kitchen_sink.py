# -*- coding: utf-8 -*-
import kivymd.snackbar as Snackbar
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from kivymd.navigationdrawer import NavigationDrawer
from kivymd.selectioncontrols import MDCheckbox
from kivymd.theming import ThemeManager
from kivymd.dialog import MDDialog
from kivymd.time_picker import MDTimePicker
from kivymd.date_picker import MDDatePicker

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import NavigationDrawer kivymd.navigationdrawer.NavigationDrawer
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import SingleLineTextField kivymd.textfields.SingleLineTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker

BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'KivyMD Kitchen Sink'
        background_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: app.nav_drawer.toggle()]]
        right_action_items: [['more-vert', lambda x: app.nav_drawer.toggle()]]
    ScreenManager:
        id: scr_mngr
        Screen:
            name: 'bottomsheet'
            MDRaisedButton:
                text: "Open list bottom sheet"
                opposite_colors: True
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                on_release: app.show_example_bottom_sheet()
            MDRaisedButton:
                text: "Open grid bottom sheet"
                opposite_colors: True
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                on_release: app.show_example_grid_bottom_sheet()
        Screen:
            name: 'button'
            MDFlatButton:
                text: 'MDFlatButton'
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.75}
            MDRaisedButton:
                text: "MDRaisedButton"
                elevation_normal: 2
                opposite_colors: True
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDFloatingActionButton:
                id:                    float_act_btn
                icon:                'plus'
                size_hint:            None, None
                size:                dp(56), dp(56)
                opposite_colors:    True
                elevation_normal:    8
                pos_hint:            {'center_x': 0.5, 'center_y': 0.25}

        Screen:
            name: 'card'
            MDCard:
                size_hint: None, None
                size:     dp(320), dp(180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            MDCard:
                size_hint: None, None
                size: dp(320), dp(180)
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                BoxLayout:
                    orientation:'vertical'
                    padding: dp(8)
                    MDLabel:
                        text: 'Title'
                        theme_text_color: 'Secondary'
                        font_style:"Title"
                        size_hint_y: None
                        height: dp(36)
                    MDSeparator:
                        height: dp(1)
                    MDLabel:
                        text: 'Body'
                        theme_text_color: 'Primary'
        Screen:
            name: 'slider'
            BoxLayout:
                MDSlider:
                    id: hslider
                    min:0
                    max:100
                    value: 10
                MDSlider:
                    id: vslider
                    orientation:'vertical'
                    min:0
                    max:100
                    value: hslider.value
        Screen:
            name: 'dialog'
            MDRaisedButton:
                text: "Open dialog"
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                opposite_colors: True
                on_release: app.show_example_dialog()
        Screen:
            name: 'grid'
            ScrollView:
                do_scroll_x: False
                GridLayout:
                    cols: 3
                    row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
                    row_force_default: True
                    size_hint_y: None
                    height: 8 * dp(100) # /1 * self.row_default_height
                    padding: dp(4), dp(4)
                    spacing: dp(4)
                    SmartTileWithLabel:
                        mipmap: True
                        source: './assets/african-lion-951778_1280.jpg'
                        text: "African Lion"
                    SmartTile:
                        mipmap: True
                        source: './assets/beautiful-931152_1280.jpg'
                    SmartTile:
                        mipmap: True
                        source: './assets/african-lion-951778_1280.jpg'
                    SmartTile:
                        mipmap: True
                        source: './assets/guitar-1139397_1280.jpg'
                    SmartTile:
                        mipmap: True
                        source: './assets/robin-944887_1280.jpg'
                    SmartTile:
                        mipmap: True
                        source: './assets/kitten-1049129_1280.jpg'
                    SmartTile:
                        mipmap: True
                        source: './assets/light-bulb-1042480_1280.jpg'
                    SmartTile:
                        mipmap: True
                        source: './assets/tangerines-1111529_1280.jpg'
        Screen:
            name: 'list'
            ScrollView:
                do_scroll_x: False
                MDList:
                    id: ml
                    OneLineListItem:
                        text: "One-line item"
                    TwoLineListItem:
                        text: "Two-line item"
                        secondary_text: "Secondary text here"
                    ThreeLineListItem:
                        text: "Three-line item"
                        secondary_text: "This is a multi-line label where you can fit more text than usual"
                    OneLineAvatarListItem:
                        text: "Single-line item with avatar"
                        AvatarSampleWidget:
                            source: './assets/avatar.png'
                    TwoLineAvatarListItem:
                        type: "two-line"
                        text: "Two-line item..."
                        secondary_text: "with avatar"
                        AvatarSampleWidget:
                            source: './assets/avatar.png'
                    ThreeLineAvatarListItem:
                        type: "three-line"
                        text: "Three-line item..."
                        secondary_text: "...with avatar..." + '\\n' + "and third line!"
                        AvatarSampleWidget:
                            source: './assets/avatar.png'
                    OneLineIconListItem:
                        text: "Single-line item with left icon"
                        IconLeftSampleWidget:
                            id: li_icon_1
                            icon: 'star-circle'
                    TwoLineIconListItem:
                        text: "Two-line item..."
                        secondary_text: "...with left icon"
                        IconLeftSampleWidget:
                            id: li_icon_2
                            icon: 'comment-text-alt'
                    ThreeLineIconListItem:
                        text: "Three-line item..."
                        secondary_text: "...with left icon..." + '\\n' + "and third line!"
                        IconLeftSampleWidget:
                            id: li_icon_3
                            icon: 'card-sd'
                    OneLineAvatarIconListItem:
                        text: "Single-line + avatar&icon"
                        AvatarSampleWidget:
                            source: './assets/avatar.png'
                        IconRightSampleWidget:
                    TwoLineAvatarIconListItem:
                        text: "Two-line item..."
                        secondary_text: "...with avatar&icon"
                        AvatarSampleWidget:
                            source: './assets/avatar.png'
                        IconRightSampleWidget:
                    ThreeLineAvatarIconListItem:
                        text: "Three-line item..."
                        secondary_text: "...with avatar&icon..." + '\\n' + "and third line!"
                        AvatarSampleWidget:
                            source: './assets/avatar.png'
                        IconRightSampleWidget:
        Screen:
            name: 'menu'
            MDRaisedButton:
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                text: 'Open menu'
                opposite_colors: True
                pos_hint: {'center_x': 0.1, 'center_y': 0.9}
                on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
            MDRaisedButton:
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                text: 'Open menu'
                opposite_colors: True
                pos_hint: {'center_x': 0.1, 'center_y': 0.1}
                on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
            MDRaisedButton:
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                text: 'Open menu'
                opposite_colors: True
                pos_hint: {'center_x': 0.9, 'center_y': 0.1}
                on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
            MDRaisedButton:
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                text: 'Open menu'
                opposite_colors: True
                pos_hint: {'center_x': 0.9, 'center_y': 0.9}
                on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
            MDRaisedButton:
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                text: 'Open menu'
                opposite_colors: True
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)

        Screen:
            name: 'progress'
            MDCheckbox:
                id:            chkbox
                size_hint:    None, None
                size:        dp(48), dp(48)
                pos_hint:    {'center_x': 0.5, 'center_y': 0.4}
                active: True
            MDSpinner:
                id: spinner
                size_hint: None, None
                size: dp(46), dp(46)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                active: True if chkbox.active else False
        Screen:
            name: 'progressbars'
            BoxLayout:
                orientation:'vertical'
                padding: '8dp'

                MDSlider:
                    id:progress_slider
                    min:0
                    max:100
                    value: 40

                MDProgressBar:
                    value: progress_slider.value
                MDProgressBar:
                    reversed: True
                    value: progress_slider.value

                BoxLayout:
                    MDProgressBar:
                        orientation:"vertical"
                        reversed: True
                        value: progress_slider.value

                    MDProgressBar:
                        orientation:"vertical"
                        value: progress_slider.value

        Screen:
            name: 'selectioncontrols'
            MDCheckbox:
                id:            grp_chkbox_1
                group:        'test'
                size_hint:    None, None
                size:        dp(48), dp(48)
                pos_hint:    {'center_x': 0.25, 'center_y': 0.5}
            MDCheckbox:
                id:            grp_chkbox_2
                group:        'test'
                size_hint:    None, None
                size:        dp(48), dp(48)
                pos_hint:    {'center_x': 0.5, 'center_y': 0.5}
            MDSwitch:
                size_hint:    None, None
                size:        dp(36), dp(48)
                pos_hint:    {'center_x': 0.75, 'center_y': 0.5}
                active:        False

        Screen:
            name: 'snackbar'
            MDRaisedButton:
                text: "Create simple snackbar"
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                opposite_colors: True
                on_release: app.show_example_snackbar('simple')
            MDRaisedButton:
                text: "Create snackbar with button"
                size_hint: None, None
                size: 4 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                opposite_colors: True
                on_release: app.show_example_snackbar('button')
            MDRaisedButton:
                text: "Create snackbar with a lot of text and a button"
                size_hint: None, None
                size: 5 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                opposite_colors: True
                on_release: app.show_example_snackbar('verylong')

        Screen:
            name: 'textfields'
            ScrollView:
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(1000)
                    BoxLayout:
                        size_hint_y: None
                        height: dp(250)
                        padding: dp(48)
                        orientation: 'vertical'
                        SingleLineTextField:
                            hint_text: "No helper text"
                        SingleLineTextField:
                            hint_text: "on_focus"
                            message: "This will disappear when you click off"
                            message_mode: "on_focus"
                        SingleLineTextField:
                            hint_text: "persistent"
                            message: "Text is always here"
                            message_mode: "persistent"
                        SingleLineTextField:
                            id: text_field_error
                            hint_text: "on_error (Hit Enter with no text here)"
                            message: "You must put something here"
                            message_mode: "on_error"

                    BoxLayout:
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Body1 label"
                            halign: 'center'
                        MDLabel:
                            font_style: 'Body2'
                            theme_text_color: 'Primary'
                            text: "Body2 label"
                            halign: 'center'
                    BoxLayout:
                        MDLabel:
                            font_style: 'Caption'
                            theme_text_color: 'Primary'
                            text: "Caption label"
                            halign: 'center'
                        MDLabel:
                            font_style: 'Subhead'
                            theme_text_color: 'Primary'
                            text: "Subhead label"
                            halign: 'center'
                    BoxLayout:
                        MDLabel:
                            font_style: 'Title'
                            theme_text_color: 'Primary'
                            text: "Title label"
                            halign: 'center'
                        MDLabel:
                            font_style: 'Headline'
                            theme_text_color: 'Primary'
                            text: "Headline label"
                            halign: 'center'
                    MDLabel:
                        font_style: 'Display1'
                        theme_text_color: 'Primary'
                        text: "Display1 label"
                        halign: 'center'
                        size_hint_y: None
                        height: self.texture_size[1] + dp(4)
                    MDLabel:
                        font_style: 'Display2'
                        theme_text_color: 'Primary'
                        text: "Display2 label"
                        halign: 'center'
                        size_hint_y: None
                        height: self.texture_size[1] + dp(4)
                    MDLabel:
                        font_style: 'Display3'
                        theme_text_color: 'Primary'
                        text: "Display3 label"
                        halign: 'center'
                        size_hint_y: None
                        height: self.texture_size[1] + dp(4)
                    MDLabel:
                        font_style: 'Display4'
                        theme_text_color: 'Primary'
                        text: "Display4 label"
                        halign: 'center'
                        size_hint_y: None
                        height: self.texture_size[1] + dp(4)
                    BoxLayout:
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Primary color"
                            halign: 'center'
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Secondary'
                            text: "Secondary color"
                            halign: 'center'
                    BoxLayout:
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Hint'
                            text: "Hint color"
                            halign: 'center'
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Error'
                            text: "Error color"
                            halign: 'center'
                    MDLabel:
                        font_style: 'Body1'
                        theme_text_color: 'Custom'
                        text_color: (0,1,0,.4)
                        text: "Custom"
                        halign: 'center'

        Screen:
            name: 'theming'
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: dp(80)
                center_y: self.parent.center_y
                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    center_x: self.parent.center_x
                    text: 'Change theme'
                    on_release: MDThemePicker().open()
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5}
                MDLabel:
                    text: "Current: " + app.theme_cls.theme_style + ", " + app.theme_cls.primary_palette
                    theme_text_color: 'Primary'
                    pos_hint: {'center_x': 0.5}
                    halign: 'center'

        Screen:
            name: 'toolbar'
            Toolbar:
                title: "Simple toolbar"
                pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                background_color: get_color_from_hex(colors['Teal']['500'])
            Toolbar:
                title: "Toolbar with right buttons"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                background_color: get_color_from_hex(colors['Amber']['700'])
                right_action_items: [['copy', lambda x: None]]
            Toolbar:
                title: "Toolbar with left and right buttons"
                pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                background_color: get_color_from_hex(colors['DeepPurple']['A400'])
                left_action_items: [['arrow-left', lambda x: None]]
                right_action_items: [['lock', lambda x: None], \
                    ['camera', lambda x: None], \
                    ['play', lambda x: None]]
        Screen:
            name: 'tabs'
            MDTabbedPanel:
                id: tab_panel
                tab_display_mode:'text'

                MDTab:
                    name: 'music' 
                    text: "Music" # Why are these not set!!!
                    icon: "playlist-audio"
                    MDLabel:
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                        text: "Here is my music list :)"
                        halign: 'center'
                MDTab:
                    name: 'movies'
                    text: 'Movies'
                    icon: "movie"
                     
                    MDLabel:
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                        text: "Show movies here :)"
                        halign: 'center'
                        
            BoxLayout:
                size_hint_y:None
                height: '48dp'
                padding: '12dp'
                MDLabel:
                    font_style: 'Body1'
                    theme_text_color: 'Primary'
                    text: "Use icons"
                    size_hint_x:None
                    width: '64dp'
                MDCheckbox:
                    on_state: tab_panel.tab_display_mode = 'icons' if tab_panel.tab_display_mode=='text' else 'text'
        Screen:
            name: 'accordion'
            BoxLayout:
                MDAccordion:
                    orientation:'vertical'
                    size_hint_x: None
                    width: '240dp'
                    MDAccordionItem:
                        id: accordion_item
                        title:'Item 1'
                        icon: 'home'
                        ScrollView:
                            MDList:
                                OneLineListItem:
                                    text: "Subitem 1"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                                OneLineListItem:
                                    text: "Subitem 2"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                                OneLineListItem:
                                    text: "Subitem 3"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                    MDAccordionItem:
                        title:'Item 2'
                        icon: 'globe'
                        ScrollView:
                            MDList:
                                OneLineListItem:
                                    text: "Subitem 4"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                                OneLineListItem:
                                    text: "Subitem 5"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                                OneLineListItem:
                                    text: "Subitem 6"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                    MDAccordionItem:
                        title:'Item 3'
                        icon: 'account'
                        ScrollView:
                            MDList:
                                OneLineListItem:
                                    text: "Subitem 7"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                                OneLineListItem:
                                    text: "Subitem 8"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                                OneLineListItem:
                                    text: "Subitem 9"
                                    theme_text_color: 'Custom'
                                    text_color: [1,1,1,1]
                MDLabel:
                    text: 'Content'
                    theme_text_color: 'Primary'
        Screen:
            name: 'pickers'
            BoxLayout:
                spacing: dp(40)
                orientation: 'vertical'
                size_hint_x: None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                BoxLayout:
                    orientation: 'vertical'
                    # size_hint: (None, None)
                    MDRaisedButton:
                        text: "Open time picker"
                        size_hint: None, None
                        size: 3 * dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        opposite_colors: True
                        on_release: app.show_example_time_picker()
                    MDLabel:
                        id: time_picker_label
                        theme_text_color: 'Primary'
                        size_hint: None, None
                        size: dp(48)*3, dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    BoxLayout:
                        size: dp(48)*3, dp(48)
                        size_hint: (None, None)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDLabel:
                            theme_text_color: 'Primary'
                            text: "Start on previous time"
                            size_hint: None, None
                            size: dp(130), dp(48)
                        MDCheckbox:
                            id: time_picker_use_previous_time
                            size_hint: None, None
                            size: dp(48), dp(48)
                BoxLayout:
                    orientation: 'vertical'
                    MDRaisedButton:
                        text: "Open date picker"
                        size_hint: None, None
                        size: 3 * dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        opposite_colors: True
                        on_release: app.show_example_date_picker()
                    MDLabel:
                        id: date_picker_label
                        theme_text_color: 'Primary'
                        size_hint: None, None
                        size: dp(48)*3, dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    BoxLayout:
                        size: dp(48)*3, dp(48)
                        size_hint: (None, None)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDLabel:
                            theme_text_color: 'Primary'
                            text: "Start on previous date"
                            size_hint: None, None
                            size: dp(130), dp(48)
                        MDCheckbox:
                            id: date_picker_use_previous_date
                            size_hint: None, None
                            size: dp(48), dp(48)

<KitchenSinkNavDrawer>
    title: "NavigationDrawer"
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Bottom sheets"
        on_release: app.root.ids.scr_mngr.current = 'bottomsheet'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Buttons"
        on_release: app.root.ids.scr_mngr.current = 'button'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Cards"
        on_release: app.root.ids.scr_mngr.current = 'card'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Dialogs"
        on_release: app.root.ids.scr_mngr.current = 'dialog'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Grid lists"
        on_release: app.root.ids.scr_mngr.current = 'grid'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Lists"
        on_release: app.root.ids.scr_mngr.current = 'list'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Menus"
        on_release: app.root.ids.scr_mngr.current = 'menu'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Progress & activity"
        on_release: app.root.ids.scr_mngr.current = 'progress'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Progress bars"
        on_release: app.root.ids.scr_mngr.current = 'progressbars'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Selection controls"
        on_release: app.root.ids.scr_mngr.current = 'selectioncontrols'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Snackbars"
        on_release: app.root.ids.scr_mngr.current = 'snackbar'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Text fields"
        on_release: app.root.ids.scr_mngr.current = 'textfields'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Themes"
        on_release: app.root.ids.scr_mngr.current = 'theming'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Toolbars"
        on_release: app.root.ids.scr_mngr.current = 'toolbar'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Sliders"
        on_release: app.root.ids.scr_mngr.current = 'slider'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Tabs"
        on_release: app.root.ids.scr_mngr.current = 'tabs'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Accordion"
        on_release: app.root.ids.scr_mngr.current = 'accordion'
    NavigationDrawerIconButton:
        icon: 'circle'
        text: "Pickers"
        on_release: app.root.ids.scr_mngr.current = 'pickers'
'''


class KitchenSinkNavDrawer(NavigationDrawer):
    pass


class KitchenSink(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()
    previous_date = ObjectProperty()

    menu_items = [
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
    ]

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        # self.theme_cls.theme_style = 'Dark'

        main_widget.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)

        self.nav_drawer = KitchenSinkNavDrawer()
        return main_widget

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar.make("This is a snackbar!")
        elif snack_type == 'button':
            Snackbar.make("This is a snackbar", button_text="with a button!",
                          button_callback=lambda *args: 2)
        elif snack_type == 'verylong':
            Snackbar.make("This is a very very very very very very very long "
                          "snackbar!",
                          button_text="Hello world")

    def show_example_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="This is a dialog with a title and some text. "
                               "That's pretty awesome right!",
                          valign='top')

        content.bind(size=content.setter('text_size'))
        self.dialog = MDDialog(title="This is a test dialog",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def get_time_picker_data(self, instance, time):
        self.root.ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        self.time_dialog = MDTimePicker()
        self.time_dialog.bind(time=self.get_time_picker_data)
        if self.root.ids.time_picker_use_previous_time.active:
            try:
                self.time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        self.time_dialog.open()

    def set_previous_date(self, date_obj):
        self.previous_date = date_obj

    def show_example_date_picker(self):
        if self.root.ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(self.set_previous_date,
                             pd.year, pd.month, pd.day).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()

    def theme_swap(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def show_example_bottom_sheet(self):
        bs = MDListBottomSheet()
        bs.add_item("Here's an item with text only", lambda x: x)
        bs.add_item("Here's an item with an icon", lambda x: x,
                    icon='account-calendar')
        bs.add_item("Here's another!", lambda x: x, icon='nfc')
        bs.open()

    def show_example_grid_bottom_sheet(self):
        bs = MDGridBottomSheet()
        bs.add_item("Facebook", lambda x: x,
                    icon_src='./assets/facebook-box.png')
        bs.add_item("YouTube", lambda x: x,
                    icon_src='./assets/youtube-play.png')
        bs.add_item("Twitter", lambda x: x,
                    icon_src='./assets/twitter.png')
        bs.add_item("Da Cloud", lambda x: x,
                    icon_src='./assets/cloud-upload.png')
        bs.add_item("Camera", lambda x: x,
                    icon_src='./assets/camera.png')
        bs.open()

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 0:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def on_pause(self):
        return True

    def on_stop(self):
        pass

    def test(self):
        self.root.ids['scr_mngr'].current = 'grid'


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


if __name__ == '__main__':
    KitchenSink().run()
