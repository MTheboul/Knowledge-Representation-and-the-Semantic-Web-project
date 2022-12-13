import {
  Typography,
  Card,
  CardContent,
  CardActions,
  Button,
} from "@mui/material";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import top100Films from "./data/movie";

export default function Config(props) {
  const { subject } = props;

  const quitQuiz = () => {
    props.updateQuizData((prevState) => ({
      ...prevState,
      started: false,
    }));
  };

  const startQuiz = () => {
    props.updateQuizData((prevState) => ({
      ...prevState,
      started: false,
    }));
  };

  return (
    <Card variant="outlined" sx={{ pt: 3, pb: 3 }}>
      <CardContent>
        <Typography
          sx={{ display: "flex", justifyContent: "center", mb: 3 }}
          variant="h4"
          color="text.secondary"
        >
          {subject}
        </Typography>
        <Autocomplete
          disablePortal
          id={"combo-box-demo" + subject}
          options={top100Films}
          sx={{ width: 300 }}
          renderInput={(params) => <TextField {...params} label={subject} />}
        />
      </CardContent>
      <CardActions sx={{ display: "flex", justifyContent: "center" }}>
        <Button onClick={startQuiz} variant="outlined">
          Start
        </Button>
        <Button onClick={quitQuiz} variant="outlined">
          Quit
        </Button>
      </CardActions>
    </Card>
  );
}
