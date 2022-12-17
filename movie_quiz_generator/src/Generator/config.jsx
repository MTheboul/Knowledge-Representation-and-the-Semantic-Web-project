import {
  Typography,
  Card,
  CardContent,
  CardActions,
  Button,
  Box,
} from "@mui/material";
import { useState } from "react";
import TextField from "@mui/material/TextField";
import LoadingButton from "@mui/lab/LoadingButton";
import Autocomplete from "@mui/material/Autocomplete";
import top100Films from "../Data/movie";
import axios from "axios";
import { Stack } from "@mui/system";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";
import top100actor from "../Data/actor";
import ListItem from "@mui/material/ListItem";
import List from "@mui/material/List";
import Alert from "@mui/material/Alert";
import IconButton from "@mui/material/IconButton";
import Collapse from "@mui/material/Collapse";
import CloseIcon from "@mui/icons-material/Close";

export default function Config(props) {
  const { quizData, updateQuizData } = props;

  const [disp, setDisp] = useState(false);
  const [error, setError] = useState("");
  const [textInput, setTextInput] = useState(
    quizData.subject === "Movie" ? top100Films[0].label : top100actor[0].label
  );
  const [isLoading, setIsLoading] = useState(false);
  const [succesOpen, setSuccesOpen] = useState(false);
  const [errorOpen, setErrorOpen] = useState(false);

  const getQuiz = () => {
    setIsLoading(true);
    axios
      .get(
        "http://127.0.0.1:5000/createQuiz" +
          quizData.subject +
          "?name=" +
          textInput
      )
      .then((data) => {
        updateQuizData((prevState) => ({
          ...prevState,
          questions: data.data,
        }));
        setSuccesOpen(true);
      })
      .catch((error) => {
        console.log(error);
        setError(error);
        setErrorOpen(true);
        // handle any errors/rejected Promises
      })
      .finally(() => {
        setIsLoading(false);
      }); // complete loading success/fail
  };

  const quitQuiz = () => {
    console.log(quizData.questions[0]);
    updateQuizData((prevState) => ({
      ...prevState,
      started: false,
      questions: {},
      config: false,
    }));
  };

  // const startQuiz = () => {
  //   console.log(quizData.subject);
  //   updateQuizData((prevState) => ({
  //     ...prevState,
  //     started: true,
  //   }));
  // };

  const exportData = () => {
    const jsonString = `data:text/json;chatset=utf-8,${encodeURIComponent(
      JSON.stringify(quizData.questions)
    )}`;
    const link = document.createElement("a");
    link.href = jsonString;
    link.download = "Quiz" + quizData.subject + ".json";

    link.click();
  };

  return (
    <Card variant="outlined" sx={{ pb: 3 }}>
      <Collapse in={succesOpen}>
        <Alert
          action={
            <IconButton
              aria-label="close"
              color="inherit"
              size="small"
              onClick={() => {
                setSuccesOpen(false);
              }}
            >
              <CloseIcon fontSize="inherit" />
            </IconButton>
          }
          sx={{ mb: 2 }}
        >
          New Question Generated!
        </Alert>
      </Collapse>
      <Collapse in={errorOpen}>
        <Alert
          color="error"
          action={
            <IconButton
              aria-label="close"
              color="error"
              size="small"
              onClick={() => {
                setErrorOpen(false);
              }}
            >
              <CloseIcon fontSize="inherit" />
            </IconButton>
          }
          sx={{ mb: 2 }}
        >
          Error: {error.message}
        </Alert>
      </Collapse>
      <CardContent>
        <Typography
          sx={{ display: "flex", justifyContent: "center", mb: 3 }}
          variant="h4"
          color="text.secondary"
        >
          {quizData.subject}
        </Typography>
        <Stack direction="row" spacing={2}>
          <Autocomplete
            disablePortal
            id={"combo-box-demo" + quizData.subject}
            options={quizData.subject === "Movie" ? top100Films : top100actor}
            sx={{ width: 300 }}
            inputValue={textInput}
            onInputChange={(event, newInputValue) => {
              setTextInput(newInputValue);
              console.log("Inputvalue: " + textInput);
            }}
            renderInput={(params) => (
              <TextField {...params} label={quizData.subject} />
            )}
          />
          <LoadingButton
            size="small"
            onClick={getQuiz}
            loading={isLoading}
            loadingIndicator="Loading…"
            variant="outlined"
          >
            Generate
          </LoadingButton>
        </Stack>
        <FormControlLabel
          sx={{
            display: "block",
          }}
          control={
            <Switch
              checked={disp}
              onChange={() => setDisp(!disp)}
              name="loading"
              color="primary"
            />
          }
          label="display"
        />
        <Box
          hidden={!disp}
          sx={{
            width: "100%",
            height: 400,
          }}
        >
          <List
            sx={{
              bgcolor: "background.paper",
              position: "fix",
              overflow: "auto",
              maxHeight: 375,
            }}
          >
            {Object.values(quizData.questions).map((question) => (
              <ListItem>
                <Card variant="outlined" sx={{ pt: 3, pb: 3, pl: 3, pr: 3 }}>
                  <Typography>{question[0]}</Typography>
                  <Typography>{question[1]}</Typography>
                </Card>
              </ListItem>
            ))}
          </List>
        </Box>
      </CardContent>
      <CardActions sx={{ display: "flex", justifyContent: "center" }}>
        <Button onClick={exportData} variant="outlined">
          Download
        </Button>
        {/* <Button
          onClick={startQuiz}
          hidden={true}
          variant="outlined"
          // disabled={quizData.questions === {}}
        >
          Start
        </Button> */}
        <Button onClick={quitQuiz} variant="outlined">
          Quit
        </Button>
      </CardActions>
    </Card>
  );
}
