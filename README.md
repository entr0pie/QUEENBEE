# 🐝 Queenbee 👑

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
<!---Incrível trabalho do iuricode. Por favor, dá um confere: https://github.com/iuricode/readme-template --->

<!--
![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)
-->

<img src="images/queenbee.png" alt="Queenbee Help Text">

> A tool to search, add and store [Beecrowd](https://www.beecrowd.com.br/judge/en) exercise resolutions. 

The project is still under development and the next updates will focus on the following tasks:

- [ ] Create an in-application update (pull, add, commit, push) mechanism;
- [ ] Sync with github repository without downloading all files (aka push without pull);
- [ ] Refactor CREATION MODE;

## 💻 Prerequisites

Before you start, make sure you've met the following requirements:
* Python 3.7 or higher;
* Colorama, BeautifulSoup4, Requests:
```
pip install colorama
pip install beautifulsoup4
pip install requests
```

## 🚀 Instaling QueenBee

Linux e macOS:
```
git clone https://github.com/entr0pie/QUEENBEE
cd QueenBee
python3 installer.py
rm installer.py
```

Windows:
```
git clone https://github.com/entr0pie/QUEENBEE
chdir QueenBee
python3 installer.py
del installer.py
```

## ☕ Using QueenBee

### ❓ Consulting an exercise:
<img src="images/search.png" alt="Search function in QueenBee">

### ❗ Adding a new resolution:
<img src="images/register.png" alt="Register Hello World Exercise">

### 🖊️ Getting the exercise prompt:
<img src="images/info.png" alt="Anyone can explain to me how to do this?">


## 🐝 Contributing with QueenBee
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
The best way to help the project is **increasing the database!** Any question that you've done (in any language!) can be added to QUEENBEE repository:
1. Register the exercise:
```
python3 queenbee.py --register my_exercise.rs
```
2. Update the local-repo:
```
git pull 
```

3. Add and push your new exercise!
```
git add .
git commit -m "My new exercise its done!"
git push 
```

<!---
1. Fork this repository.
2. Create an branch: `git checkout -b branch`.
3. Do your modifications and confirm: `git commit -m message`
4. Send it to the original branch: `git push origin QueenBee / branch`
5. Create pull request

As an alternative, search for pull solicitations on [Github Oficial Docs](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
--->
<!--
## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars3.githubusercontent.com/u/31936044" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Iuri Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://s2.glbimg.com/FUcw2usZfSTL6yCCGj3L3v3SpJ8=/smart/e.glbimg.com/og/ed/f/original/2019/04/25/zuckerberg_podcast.jpg" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Mark Zuckerberg</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 😄 Seja um dos contribuidores<br>

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.
-->

## 📝 License

This project is under GNU General License. More information [here](LICENSE).


[⬆ Back to the top](#QueenBee)<br>
