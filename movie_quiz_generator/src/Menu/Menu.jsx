import Grid from "@mui/material/Grid";
import Quiz from "../Quiz/Quiz";
import { useState } from "react";
import { CssBaseline, Box, Container } from "@mui/material";
import { grey } from "@mui/material/colors";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import QuizCard from "./QuizCard";
import Config from "../Generator/config";

function Menu() {
  const [quizData, setquizData] = useState({
    subject: "",
    name: "",
    questions: {},
    started: false,
    config: false,
    questionNumber: 4,
  });
  return (
    <div>
      <CssBaseline />
      <Box
        style={{ overflowY: "scroll" }}
        sx={{
          backgroundColor: grey[400],
          height: "100vh",
          display: "flex",
          alignItems: "center",
        }}
      >
        {quizData.started ? (
          <Container maxWidth="sm">
            <Quiz quizData={quizData} updateQuizData={setquizData} />
          </Container>
        ) : quizData.config ? (
          <Container maxWidth="sm">
            <Config quizData={quizData} updateQuizData={setquizData} />
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
              <Grid
                container
                spacing={5}
                direction="row"
                alignItems="center"
                justifyContent="center"
              >
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
                    description="a series of questions based on different Movie"
                    imagePath="movie.png"
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

export default Menu;
