<html>
<meta charset="UTF-8">
<body> 
<H1>Домашнее задание # 11 по курсу OTUS</H1> 
<P>С помощью GraphQL создать схему</P> 
<div>
Для того, чтобы посмотреть все курсы, их студентов и преподавателей, необходимо 
зайти на страницу http://127.0.0.1:8000/graphql/ и ввести запрос 
query{
  allCourses{
    id
    title
    teachers{
      firstName
    	lastName
    }
    students{
      firstName
    	lastName
    }
    }
}
</div>
</body> 
</html>