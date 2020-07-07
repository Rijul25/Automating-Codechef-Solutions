#!/usr/bin/env python
# coding: utf-8

# In[22]:


from selenium import webdriver


# In[23]:


browser = webdriver.Chrome("./Downloads/chromedriver")


# In[24]:


browser.get("https://codechef.com")


# In[25]:


username_element = browser.find_element_by_id("edit-name")


# In[26]:


username_element.send_keys("rijul_25")


# In[27]:


password_element = browser.find_element_by_id("edit-pass")


# In[28]:


from getpass import getpass


# In[29]:


password_element.send_keys(getpass("Enter password"))


# In[30]:


browser.find_element_by_id("edit-submit").click()


# In[39]:


browser.get("https://www.codechef.com/submit/RAINBOWA")


# In[40]:


browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


# In[34]:


with open("./rainbow.cpp", 'r') as f:
    code = f.read()


# In[35]:


code_element = browser.find_element_by_id('edit-program')


# In[36]:


code_element.send_keys(code)


# In[41]:


browser.find_element_by_xpath('//*[@id="edit-language"]/option[9]').click()


# In[42]:


browser.find_element_by_id("edit-submit").click()

