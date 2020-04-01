# rod_bot

Bot to aim children to make homework and keep on learning

## Roles

- **Bot**, will give an answer to students in the following cases:

  - Welcome the student when (s)he logs in.
  - Tell the student at what point in the motivational story is and wich is the goal for the day.
  - Will tell the student the tasks (s)he should do every day and how they will help to achieve the daily goal.
  - Correct the answers the student gives to simple questions, sucha as sums, substractions, English vocabulary, ...
  - Save students credentials, emotions, marks, tasks, ...

* **Parent/teacher**

  - Should be able to upload the daily tasks.
  - Receive a notification when the student has finished any task.
  - Evaluate tasks and get the daily marks.
  - Get the summary of grades in a certain period of time.
  - Create a story depending on the topics and the subjects the students are working on.

* **Student**

  - Answer simple questions the bot makes.
  - Choose the order in wich (s)he will make daily tasks.
  - Get the results of simple exercises.
  - Get the evolution of the story.

## Flow example

---

<div style="text-align: right"> <strong>Student</strong>: Hola Rodbot </div>

**RodBot**: Buenos días, Fulanito ¿Cómo te encuentras hoy?:

- Muy bien
- Alegre
- Emocionado
- Cansado
- Preocupado

<div style="text-align: right"> <strong>Student</strong>: Bien </div>

**RB**: Me alegro. Estás son tus tareas para hoy:

- [Ficha de MATEMÁTICAS](https://drive.google.com/open?id=1oo-2a8bV55DmiCmS9GnZ019Agi1bX8WA)
- [Ejercicios de INGLÉS](https://www.blinklearning.com/LMS/busqueda.php?&student=1)
- [Dictado](speech.py)
- [Plástica](https://drive.google.com/open?id=1f2uTCglxzKDAxHv8OPPbUYNUk6ffwyUw)

¿Cuál quieres hacer primero? Recuerda que es mejor dejar lo más fácil y lo que más te gusta para el final.

<div style="text-align: right"><em>
El chaval pulsa en dictado<br>
Se reproduce el dictado<br>
Vuelve a salir el listado de tareas pendientes</em></div>

**RB**: Estas son las tareas pendientes:

- [Ficha de MATEMÁTICAS](https://drive.google.com/open?id=1oo-2a8bV55DmiCmS9GnZ019Agi1bX8WA)
- [Ejercicios de INGLÉS](https://www.blinklearning.com/LMS/busqueda.php?&student=1)
- [Plástica](https://drive.google.com/open?id=1f2uTCglxzKDAxHv8OPPbUYNUk6ffwyUw)

¿Cuál harás ahora?

---

For Natural and Social Sciences hay que especificar el modo en que se plantearán los contenidos.
