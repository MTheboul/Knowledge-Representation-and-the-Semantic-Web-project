import Grid from "@mui/material/Grid";
import Quiz from "./Quiz";
import { useState } from "react";
import { CssBaseline, Box, Container } from "@mui/material";
import { grey } from "@mui/material/colors";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import QuizCard from "./QuizCard";

function App() {
  const [quizData, setquizData] = useState({
    subject: "",
    started: false,
    questionNumber: 4,
  });
  return (
    <div>
      <CssBaseline />
      <Box
        sx={{
          backgroundColor: grey[400],
          height: "100vh",
          display: "flex",
          alignItems: "center",
        }}
      >
        {quizData.started ? (
          <Container maxWidth="sm">
            <Quiz updateQuizData={setquizData} />
          </Container>
        ) : (
          <Container>
            <Box spacing={5}>
              <Card variant="outlined" justify="center">
                <CardContent sx={{ justifyContent: "center" }}>
                  <Typography
                    gutterBottom
                    variant="h4"
                    component="div"
                    align="center"
                  >
                    Generate a Quiz
                  </Typography>
                </CardContent>
              </Card>
              <Box pt={3} />
              <Grid container spacing={5} justify="center">
                <Grid item xs={4}>
                  <QuizCard
                    subject="Actors"
                    description="a series of questions based on different actors"
                    imagePath="Actore.png"
                    updateQuizData={setquizData}
                  />
                </Grid>
                <Grid item xs={4}>
                  <QuizCard
                    subject="Movie"
                    description="TODO description"
                    imagePath="movie.png"
                    updateQuizData={setquizData}
                  />
                </Grid>
                <Grid item xs={4}>
                  <QuizCard
                    subject="Genre"
                    description="TODO description"
                    imagePath="genre.png"
                    updateQuizData={setquizData}
                  />
                </Grid>
              </Grid>
            </Box>
          </Container>
        )}
      </Box>
    </div>
  );
}

export default App;
