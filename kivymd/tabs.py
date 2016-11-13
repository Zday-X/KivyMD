# Created on Jul 8, 2016
#
# The default kivy tab implementation seems like a stupid design to me. The
# ScreenManager is much better.
#
# @author: jrm

from kivy.properties import StringProperty, DictProperty, ListProperty, \
    ObjectProperty, OptionProperty, BoundedNumericProperty, NumericProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.backgroundcolorbehavior import BackgroundColorBehavior
from kivymd.button import MDFlatButton, BaseFlatButton, BasePressedButton
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.logger import Logger

KIVYMD_BOTTOMNAV_LAST_SIZE = 0

Builder.load_string("""
#:import sm kivy.uix.screenmanager
<MDTabbedPanel>:
    id: panel
    orientation: 'vertical' if panel.tab_orientation in ['top','bottom'] else 'horizontal'
    ScrollView:
        id: scroll_view
        size_hint_y: None
        height: panel._tab_display_height[panel.tab_display_mode]
        MDTabBar:
            id: tab_bar
            size_hint_y: None
            height: panel._tab_display_height[panel.tab_display_mode]
            background_color: panel.tab_color or panel.theme_cls.primary_color
            canvas:
                # Draw bottom border
                Color:
                    rgba: (panel.tab_border_color or panel.tab_color or panel.theme_cls.primary_dark)
                Rectangle:
                    size: (self.width,dp(2))
    ScreenManager:
        id: tab_manager
        current: root.current
        screens: root.tabs
            

<MDTabHeader>:
    canvas:
        Color:
            rgba: self.panel.tab_color or self.panel.theme_cls.primary_color
        Rectangle:
            size: self.size
            pos: self.pos
            
        # Draw indicator
        Color:
            rgba: (self.panel.tab_indicator_color or self.panel.theme_cls.accent_color) if self.tab \
                and self.tab.manager and self.tab.manager.current==self.tab.name else (self.panel.tab_border_color  \
                or self.panel.tab_color or self.panel.theme_cls.primary_dark)
        Rectangle:
            size: (self.width,dp(2))
            pos: self.pos
            
    size_hint: (None,None) #(1, None)  if self.panel.tab_width_mode=='fixed' else (None,None)
    width: (_label.texture_size[0] + dp(16))
    padding: (dp(12), 0)
    theme_text_color: 'Custom'
    text_color: (self.panel.tab_text_color_active or app.theme_cls.bg_light if app.theme_cls.theme_style == "Light" \
            else app.theme_cls.opposite_bg_light) if self.tab and self.tab.manager \
            and self.tab.manager.current==self.tab.name else (self.panel.tab_text_color \
            or self.panel.theme_cls.primary_light)
    on_press: 
        self.tab.dispatch('on_tab_press') 
        # self.tab.manager.current = self.tab.name
    on_release: self.tab.dispatch('on_tab_release')
    on_touch_down: self.tab.dispatch('on_tab_touch_down',*args)
    on_touch_move: self.tab.dispatch('on_tab_touch_move',*args)
    on_touch_up: self.tab.dispatch('on_tab_touch_up',*args)
    
    
    MDLabel:
        id: _label
        text: root.tab.text if root.panel.tab_display_mode == 'text' else u"{}".format(md_icons[root.tab.icon])
        font_style: 'Button' if root.panel.tab_display_mode == 'text' else 'Icon'
        size_hint_x: None# if root.panel.tab_width_mode=='fixed' else 1
        text_size: (None, root.height)
        height: self.texture_size[1]
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors


<MDBottomNavigation>:
    id: panel
    orientation: 'vertical'
    height: dp(56)  # Spec
    ScreenManager:
        id: tab_manager
        # transition: sm.FadeTransition() TODO: Should use FadeTransition, but it doesn't like KivyMD
        current: root.current
        screens: root.tabs
    MDBottomNavigationBar:
        size_hint_y: None
        height: dp(56)  # Spec
        background_color: root.theme_cls.bg_dark
        # anchor_x: 'center'
        # anchor_y: 'center'
        BoxLayout:
            pos_hint: {'center_x': .5, 'center_y': .5}
            id: tab_bar
            height: dp(56)
            pos: self.pos
            size_hint_x: None
            size_hint: None, None


<MDBottomNavigationHeader>:
    canvas:
        Color:
            rgba: self.panel.theme_cls.bg_dark
        Rectangle:
            size: self.size
            pos: self.pos


    # size_hint: (None,None) #(1, None)  if self.panel.tab_width_mode=='fixed' else (None,None)
    width: root.panel.width / len(root.panel.ids.tab_manager.screens) if len(root.panel.ids.tab_manager.screens) != 0 else root.panel.width
    padding: (dp(12), dp(12))
    # width: dp(1000)
    on_press:
        self.tab.dispatch('on_tab_press')
    on_release: self.tab.dispatch('on_tab_release')
    on_touch_down: self.tab.dispatch('on_tab_touch_down',*args)
    on_touch_move: self.tab.dispatch('on_tab_touch_move',*args)
    on_touch_up: self.tab.dispatch('on_tab_touch_up',*args)


    MDLabel:
        id: _label_icon
        text: u"{}".format(md_icons[root.tab.icon])
        font_style: 'Icon'
        size_hint_x: None# if root.panel.tab_width_mode=='fixed' else 1
        text_size: (None, root.height)
        height: self.texture_size[1]
        theme_text_color: 'Custom'
        text_color: root._current_color
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors
        pos: [self.pos[0], self.pos[1]]

    MDLabel:
        id: _label
        text: root.tab.text
        font_style: 'Button'
        size_hint_x: None# if root.panel.tab_width_mode=='fixed' else 1
        text_size: (None, root.height)
        height: self.texture_size[1]
        theme_text_color: 'Custom'
        text_color: root._current_color
        valign: 'bottom'
        halign: 'center'
        opposite_colors: root.opposite_colors
        font_size: root._label_font_size





<BaseRectangularButtonHACKED>:
    canvas:
        Color:
            rgba: self._current_button_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: (dp(2),)
    content: content
    theme_text_color: 'Primary'
    MDLabel:
        id: content
        text: root._capitalized_text
        font_style: 'Button'
        size_hint_x: None
        text_size: (None, root.height)
        height: self.texture_size[1]
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        disabled: root.disabled
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors

""")


class MDTabBar(ThemableBehavior, BackgroundColorBehavior, BoxLayout):
    pass


class MDBottomNavigationBar(ThemableBehavior, BackgroundColorBehavior, FloatLayout, RectangularElevationBehavior):
    pass


class MDTabHeader(MDFlatButton):
    """ Internal widget for headers based on MDFlatButton"""
    
    width = BoundedNumericProperty(dp(None), min=dp(72), max=dp(264), errorhandler=lambda x: dp(72))
    tab = ObjectProperty(None)
    panel = ObjectProperty(None)


def small_error_warn(x):
    global KIVYMD_BOTTOMNAV_LAST_SIZE
    if x < dp(80):
        if KIVYMD_BOTTOMNAV_LAST_SIZE != x:
            KIVYMD_BOTTOMNAV_LAST_SIZE = x
            Logger.warning("MDBottomNavigation: {}dp is less than the minimum size of 80dp for a "
                           "MDBottomNavigationItem, keeping the size at 80dp".format(x))
        return dp(80)
    return dp(168)


class MDBottomNavigationHeader(BaseFlatButton, BasePressedButton):
    width = BoundedNumericProperty(dp(None), min=dp(80), max=dp(168), errorhandler=lambda x: small_error_warn(x))
    tab = ObjectProperty(None)
    panel = ObjectProperty(None)
    _label = ObjectProperty()
    _label_font_size = NumericProperty(sp(12))
    _current_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    text = StringProperty('')
    _capitalized_text = StringProperty('')

    def on_text(self, instance, value):
        self._capitalized_text = value.upper()

    def __init__(self, panel, height, tab):
        self.panel = panel
        self.height = height
        self.tab = tab
        super(MDBottomNavigationHeader, self).__init__()
        self._current_color = self.theme_cls.disabled_hint_text_color
        self._label = self.ids._label
        # self.bind(_label_font_size=self._label.setter('font_size'))
        self._label_font_size = sp(12)

    def on_press(self):
        Animation(_label_font_size=sp(14), d=0.1).start(self)
        Animation(_current_color=self.theme_cls.primary_color, d=0.1).start(self)


class MDTab(Screen):
    """ A tab is simply a screen with meta information
        that defines the content that goes in the tab header.
    """
    __events__ = ('on_tab_touch_down', 'on_tab_touch_move', 'on_tab_touch_up', 'on_tab_press', 'on_tab_release')
    
    # Tab header text
    text = StringProperty("")
    
    # Tab header icon
    icon = StringProperty("checkbox-blank-circle")
    
    # Tab dropdown menu items
    menu_items = ListProperty()
    
    # Tab dropdown menu (if you want to customize it)
    menu = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(MDTab, self).__init__(**kwargs)
        self.index = 0
        self.parent_widget = None
        self.register_event_type('on_tab_touch_down')
        self.register_event_type('on_tab_touch_move')
        self.register_event_type('on_tab_touch_up')
        self.register_event_type('on_tab_press')
        self.register_event_type('on_tab_release')

    def on_leave(self, *args):
        self.parent_widget.ids.tab_manager.transition.direction = self.parent_widget.prev_dir
        
    def on_tab_touch_down(self, *args):
        pass
    
    def on_tab_touch_move(self, *args):
        pass
    
    def on_tab_touch_up(self, *args):
        pass

    def on_tab_press(self, *args):
        par = self.parent_widget
        if par.previous_tab is not self:
            par.prev_dir = str(par.ids.tab_manager.transition.direction)
            if par.previous_tab.index > self.index:
                par.ids.tab_manager.transition.direction = "right"
            elif par.previous_tab.index < self.index:
                par.ids.tab_manager.transition.direction = "left"
            par.ids.tab_manager.current = self.name
            par.previous_tab = self
    
    def on_tab_release(self, *args):
        pass
    
    def __repr__(self):
        return "<MDTab name='{}', text='{}'>".format(self.name, self.text)


class MDBottomNavigationItem(MDTab):
    header = ObjectProperty()

    def on_tab_press(self, *args):
        par = self.parent_widget
        par.ids.tab_manager.current = self.name
        if par.previous_tab is not self:
            Animation(_label_font_size=sp(12), d=0.1).start(par.previous_tab.header)
            Animation(_current_color=par.previous_tab.header.theme_cls.disabled_hint_text_color, d=0.1).start(par.previous_tab.header)
        par.previous_tab = self

    def on_leave(self, *args):
        pass


class TabbedPanelBase(ThemableBehavior, BackgroundColorBehavior, BoxLayout):
    """
    A class that contains all variables a TabPannel must have
    It is here so I (zingballyhoo) don't get mad about the TabbedPannels not being DRY
    """
    tabs = ListProperty([])

    # Current tab name
    current = StringProperty(None)

    previous_tab = ObjectProperty(None)


class MDTabbedPanel(TabbedPanelBase):
    """ A tab panel that is implemented by delegating all tabs
        to a ScreenManager.
    """
    # If tabs should fill space
    tab_width_mode = OptionProperty('stacked', options=['stacked', 'fixed'])

    # Where the tabs go
    tab_orientation = OptionProperty('top', options=['top'])  # ,'left','bottom','right'])

    # How tabs are displayed
    tab_display_mode = OptionProperty('text', options=['text', 'icons'])  # ,'both'])
    _tab_display_height = DictProperty({'text': dp(46), 'icons': dp(46), 'both': dp(72)})

    # Tab background color (leave empty for theme color)
    tab_color = ListProperty([])

    # Tab text color in normal state (leave empty for theme color)
    tab_text_color = ListProperty([])

    # Tab text color in active state (leave empty for theme color)
    tab_text_color_active = ListProperty([])

    # Tab indicator color  (leave empty for theme color)
    tab_indicator_color = ListProperty([])

    # Tab bar bottom border color (leave empty for theme color)
    tab_border_color = ListProperty([])
    
    def __init__(self, **kwargs):
        super(MDTabbedPanel, self).__init__(**kwargs)
        self.prev_dir = None
        self.index = 0
        self._refresh_tabs()
        
    def on_tab_width_mode(self, *args):
        self._refresh_tabs()
    
    def on_tab_display_mode(self, *args):
        self._refresh_tabs()
    
    def _refresh_tabs(self):
        """ Refresh all tabs """
        # if fixed width, use a box layout
        if not self.ids:
            return
        tab_bar = self.ids.tab_bar
        tab_bar.clear_widgets()
        tab_manager = self.ids.tab_manager
        for tab in tab_manager.screens:
            tab_header = MDTabHeader(tab=tab,
                                     panel=self,
                                     height=tab_bar.height)
            tab_bar.add_widget(tab_header)

    def add_widget(self, widget, **kwargs):
        """ Add tabs to the screen or the layout.
        :param widget: The widget to add.
        """
        if isinstance(widget, MDTab):
            self.index += 1
            if self.index == 1:
                self.previous_tab = widget
            widget.index = self.index
            widget.parent_widget = self
            self.ids.tab_manager.add_widget(widget)
            self._refresh_tabs()
        else:
            super(MDTabbedPanel, self).add_widget(widget)
        
    def remove_widget(self, widget):
        """ Remove tabs from the screen or the layout.
        :param widget: The widget to remove.
        """
        self.index -= 1
        if isinstance(widget, MDTab):
            self.ids.tab_manager.remove_widget(widget)
            self._refresh_tabs()
        else:
            super(MDTabbedPanel, self).remove_widget(widget)


class MDBottomNavigation(TabbedPanelBase):
    """ A bottom navigation that is implemented by delegating all items to a ScreenManager."""

    first_widget = ObjectProperty()

    # TODO: Future shifting mode: https://material-design.storage.googleapis.com/publish/material_v_9/0B3321sZLoP_HUEw4c19NVjFxNDQ/components_bottomnavigation_spec_shiftingbottomnav.webm
    # mode = OptionProperty('fixed', options=['fixed', 'shifting'])

    def __init__(self, **kwargs):
        super(MDBottomNavigation, self).__init__(**kwargs)
        self.previous_tab = None
        self.widget_index = 0
        self._refresh_tabs()
        Window.bind(on_resize=self.on_resize)

    def _refresh_tabs(self):
        """ Refresh all tabs """
        # if fixed width, use a box layout
        if not self.ids:
            return
        tab_bar = self.ids.tab_bar
        tab_bar.clear_widgets()
        tab_manager = self.ids.tab_manager
        for tab in tab_manager.screens:
            tab_header = MDBottomNavigationHeader(tab=tab,
                                                  panel=self,
                                                  height=tab_bar.height)
            tab.header = tab_header
            tab_bar.add_widget(tab_header)
            if tab is self.first_widget:
                tab_header._current_color = self.theme_cls.primary_color
                tab_header._label_font_size = sp(14)
            else:
                tab_header._label_font_size = sp(12)
        self.on_resize()

    def on_resize(self, instance=None, width=None, do_again=True):
        full_width = 0
        for tab in self.ids.tab_manager.screens:
            full_width += tab.header.width
        self.ids.tab_bar.width = full_width
        if do_again:
            Clock.schedule_once(lambda x: self.on_resize(do_again=False), 0.01)

    def add_widget(self, widget, **kwargs):
        """ Add tabs to the screen or the layout.
        :param widget: The widget to add.
        """
        if isinstance(widget, MDBottomNavigationItem):
            self.widget_index += 1
            widget.index = self.widget_index
            widget.parent_widget = self
            tab_header = MDBottomNavigationHeader(tab=widget,
                                                  panel=self,
                                                  height=widget.height)
            self.ids.tab_bar.add_widget(tab_header)
            widget.header = tab_header
            self.ids.tab_manager.add_widget(widget)
            if self.widget_index == 1:
                self.previous_tab = widget
                tab_header._current_color = self.theme_cls.primary_color
                tab_header._label_font_size = sp(14)
                self.first_widget = widget
            else:
                tab_header._label_font_size = sp(12)

            self._refresh_tabs()
        else:
            super(MDBottomNavigation, self).add_widget(widget)

        
if __name__ == '__main__':
    from kivy.app import App
    from kivymd.theming import ThemeManager
    
    class TabsApp(App):
        theme_cls = ThemeManager()

        def build(self):
            from kivy.core.window import Window
            Window.size = (540, 720)
            # self.theme_cls.theme_style = 'Dark'

            return Builder.load_string("""
#:import Toolbar kivymd.toolbar.Toolbar
#:import Snackbar kivymd.snackbar.make
#:import MDRaisedButton kivymd.button.MDRaisedButton
BoxLayout:
    orientation:'vertical'
    Toolbar:
        id: toolbar
        title: 'Page title'
        background_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: '']]
        right_action_items: [['account-search', lambda x: ''],['dots-vertical',lambda x:'']]
    MDTabbedPanel:
        id: tab_mgr
        tab_display_mode:'icons'
        
        MDTab:
            name: 'music' 
            text: "Music"
            icon: "playlist-play"
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

    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'music'
            text: "Music"
            icon: "playlist-play"
            FloatLayout:
                MDRaisedButton:
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    text: "Open theme picker"
                    # on_release: MDThemePicker().open()
                    text: "Open test snackbar"
                    on_press: Snackbar(text="This is a test snackbar")
        MDBottomNavigationItem:
            name: 'movies'
            text: 'Movies'
            icon: "movie"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "Show movies here :)"
                halign: 'center'
        MDBottomNavigationItem:
            name: 'files1'
            text: "Files"
            icon: "file"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "all of the files"
                halign: 'center'
        MDBottomNavigationItem:
            name: 'files2'
            text: "Files"
            icon: "file"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "all of the files"
                halign: 'center'
        MDBottomNavigationItem:
            name: 'files3'
            text: "Files"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "all of the files"
                halign: 'center'
     
        
""")
            

    TabsApp().run()
