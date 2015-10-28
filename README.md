# FindInDictionary
This repository contains a program, written in Python. This program searches the meaning of a word from the web and give you the results. You now don't need to open a browser and go to some online dictionaries. Just install this program and type a keyword <code>defn</code> in the Command Prompt followed by the search term and you'll get your results.
<br><br>
#Minimum Requirements:
<ol>
  <li>OS: <b>Windows</b></li>
  <li><b>Python 3.x</b>. If you don't have Python, go to: <a href="http://www.python.org">www.python.org</a> to download it.</li>
  <li>Python modules -- <b>Requests</b>, <b>BeautifulSoup4</b>. If these are not installed then go to Command Prompt and type <code>pip install requests</code> &amp; <code>pip install bs4</code>.</li>
</ol>
That's all you need!
<br>
#How to install it:
<ol>
  <li>Edit the <code>defn_batch.bat</code> - the path of defn.py is given <code>E:\Experiments\Repos\FindInDictionary\defn.py</code>. Replace it with the address of <code>defn.py</code> file on your computer.
  <li>Now you need to Edit <b>Environment Variable</b> - <code>PATH</code>. This will help you to run <b>defn.py</b> file via Command Prompt. To do this, follow the given steps:
    <ol>
      <li>Right-click <b>My Computer</b> followed by <b>Properties</b></li>
      <li>Click <b>Advanced System Properties</b></li>
      <li>Click <b>Environment Variables...</b></li>
      <li>Edit <b>PATH</b> variable: Add <code>;</code> at the last and then, the address of the directory, where the `batch` & `python` file is stored.</li>
    </ol>
  </li>
</ol>

Now you're done. Just go to Command Prompt and type (while your PC is connected to internet): <code>defn tweet</code> and see the magic happen.

Hope you'll like this. Please fork this repository to contribute, just to quench our mutual curiosity. Further improvement will done soon.

If you found any issue with this program, please report to this GitHub account, or mail to: <a href="mailto:shuvamkshah28@gmail.com">shuvamkshah28@gmail.com</a>
